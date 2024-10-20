import streamlit as st

slide_window = 7  # How many conversations to remember for context

def initialize_messages():
    """Initialize or reset chat history."""
    if st.session_state.clear_conversation or "messages" not in st.session_state:
        st.session_state.messages = []

    # Initialize the session state for emotion history if not already set
    if 'emotion_history' not in st.session_state:
        st.session_state.emotion_history = []

def configure_options():
    """Sidebar configuration options for model and session management."""
    st.sidebar.selectbox(
        'Select your model:',
        #['llama3.1-405b','reka-core','mistral-large2', 'snowflake-arctic', 'mistral-large', 'llama3-8b', 'reka-flash', 'jamba-1.5-large', 'gemma-7b'],
        ['mixtral-8x7b', 'snowflake-arctic', 'mistral-large', 'llama3-8b','llama3-70b', 'reka-flash', 'mistral-7b', 'llama2-70b-chat', 'gemma-7b'],
        key="model_name"
    )
    st.sidebar.checkbox('Remember chat history?', key="use_chat_history", value=True)
    st.sidebar.checkbox('Debug: Show summary of previous conversations', key="debug", value=True)
    st.sidebar.button("Start Over", key="clear_conversation")
    st.sidebar.expander("Session State").write(st.session_state)

def get_chat_history():
    """Retrieve the chat history based on the defined slide window."""
    return [msg for msg in st.session_state.messages[-slide_window:]]
