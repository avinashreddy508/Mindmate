import streamlit as st
import configparser
from snowflake.snowpark import Session
from helpers.chat_helper import initialize_messages, configure_options, get_chat_history

# Default Configuration
num_chunks = 3  # Number of chunks to provide as context

def create_session():
    """Create a Snowflake session using configuration details."""
    config = configparser.ConfigParser()
    config.read('config/properties.ini')
    snowflake_config = config['Snowflake']

    connection_params = {key: snowflake_config.get(key) for key in
                         ['account', 'user', 'password', 'role', 'warehouse', 'database', 'schema']}
    session = Session.builder.configs(connection_params).create()
    return session

def query_available_docs(session):
    """Query Snowflake to list available documents from a stage."""
    return session.sql("ls @mystage").collect()

def complete_response(session, question, rag):
    """Generate the AI response and incorporate emotion analysis and CBT techniques."""

    prompt, url_link, relative_path = create_prompt(session, question, rag)
    response = session.sql("SELECT snowflake.cortex.complete(?, ?)", params=[st.session_state.model_name, prompt]).collect()

    return response[0]['SNOWFLAKE.CORTEX.COMPLETE(?, ?)'], url_link, relative_path

def create_prompt(session, question, rag):
    """Create the prompt used to query the Snowflake LLM, with or without RAG."""
    if rag:
        prompt_context, relative_path = get_similar_chunks(session, question)
        prompt = f"""
            You are an expert assistant that extracts information from the provided CONTEXT.
            The CONTEXT is between <context> and </context> tags, and the chat history is between
            <chat_history> and </chat_history> tags.

            If you don't have the information, simply state so.
            <chat_history>{get_chat_history()}</chat_history>
            <context>{prompt_context}</context>
            <question>{question}</question>
        """
    else:
        prompt = f"""
         'Question:  
           {question} 
           Answer: '
        """
        relative_path = "None"

    return prompt, None, relative_path

def get_similar_chunks(session, question):
    """Retrieve the most similar document chunks for the provided question."""
    query = """
        WITH results AS (
            SELECT RELATIVE_PATH,
                   VECTOR_COSINE_SIMILARITY(docs_chunks_table.chunk_vec, 
                   SNOWFLAKE.CORTEX.EMBED_TEXT_768('e5-base-v2', ?)) AS similarity,
                   chunk
            FROM docs_chunks_table
            ORDER BY similarity DESC
            LIMIT ?
        )
        SELECT chunk, relative_path FROM results
    """
    df_chunks = session.sql(query, params=[question, num_chunks]).to_pandas()
    similar_chunks = "".join([df_chunks._get_value(i, 'CHUNK') for i in range(len(df_chunks) - 1)])
    return similar_chunks.replace("'", ""), df_chunks._get_value(0, 'RELATIVE_PATH')
