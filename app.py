import streamlit as st
from helpers.snowflake_helper import create_session, query_available_docs, complete_response
from helpers.chat_helper import initialize_messages, configure_options
from snowflake.connector.errors import ProgrammingError
from snowflake.snowpark.exceptions import SnowparkSessionException,SnowparkSQLException, SnowparkClientException


st.set_page_config(
    page_title="MindMate App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Welcome to MindMate! A powerful app for mental wellness."
    }
)

st.sidebar.image("MindMate-Chat-Assistant_.jpeg", caption="MindMate Chat Assistant", use_column_width=True)

#pd.set_option("max_colwidth", None)

# Main function for the Streamlit app
def main():
    st.title(f":speech_balloon: Meet MindMate: Your 24/7 Companion for Mental Wellness, Empowering Urban Health 🌟")

    # Set up Snowflake session
    session = create_session()

    # Sidebar settings for emotion threshold and RAG toggle
    with st.sidebar:
        st.write("Configuration Settings")
        rag = st.checkbox('Use your own documents as context?')

    # Expander to display available documents
    with st.expander("Show available documents"):
        st.write("Available documents:")
        available_docs = query_available_docs(session)
        st.dataframe([doc["name"] for doc in available_docs])

    # Initialize sidebar options and chat messages
    configure_options()
    initialize_messages()

    # Display chat messages in session
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input
    if user_question:= st.chat_input("What would you like to discuss today? (e.g., mental health, well-being)"):
        st.session_state.messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)

        # Display assistant's response with a loading spinner
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            sanitized_question = user_question.replace("'", "")
            with st.spinner(f"{st.session_state.model_name} is thinking..."):
                try:
                    response, url_link, relative_path = complete_response(session, sanitized_question, rag)
                    message_placeholder.markdown(response)

                    if rag:
                        st.markdown(f"Link to [{relative_path}]({url_link})")
                except (ProgrammingError, SnowparkSessionException,SnowparkSQLException) as e:
                     st.error("Warehouse is suspended . Please reach out for assistance or demo."
                        "Contact: avinashreddy508@gmail.com.")

        # Store the assistant's response and emotion analysis in the session history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
