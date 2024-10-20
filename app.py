import streamlit as st
import pandas as pd
from datetime import datetime
from helpers.snowflake_helper import create_session, query_available_docs, complete_response
from helpers.emotion_helper import analyze_emotion, get_cbt_techniques, get_default_cbt
from helpers.plotting_helper import plot_emotion_distribution
from helpers.chat_helper import initialize_messages, configure_options, get_chat_history

st.set_page_config(
    page_title="MindMate App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *MindMate* cool app!"
    }
)

#st.logo("MindMate-Chat-Assistant_.jpeg","medium")
#st.image("MindMate-Chat-Assistant_.jpeg", caption=None, width=200,  clamp=False, channels="RGB", output_format="auto")
#st.markdown("<h1 style='text-align: center;'>MindMate Chat Assistant</h1>", unsafe_allow_html=True)
# col1, col2, col3 = st.columns(3)
# with col2:
#     st.image("MindMate-Chat-Assistant_.jpeg", caption=None, width=250)
st.sidebar.image("MindMate-Chat-Assistant_.jpeg", caption="MindMate Chat Assistant", use_column_width=True)

#st.image("MindMate-Chat-Assistant_.jpeg", caption="MindMate Chat Assistant", width=300)
pd.set_option("max_colwidth", None)

#st.title("# Welcome to MindMate! 👋")

# Streamlit app main function
def main():
    #st.title(":speech_balloon: MindMate Chat Assistant ")
    # st.title(
    #     f":speech_balloon: Introducing MindMate, your 24/7 mental health companion for Enhancing Urban Health 👋")
    st.title(f":speech_balloon: Meet MindMate: Your 24/7 Companion for Mental Wellness, Empowering Urban Health 🌟")

    # Initialize Snowflake session
    session = create_session()

    # Sidebar: Emotion threshold and RAG toggle
    with st.sidebar:
        st.write("Configure Settings")
        # emotion_threshold = st.slider("Set Emotion Confidence Threshold for CBT (0.0 to 1.0):", 0.0, 1.0, 0.7)
        rag = st.checkbox('Use your own documents as context?')

    # Expander: Available documents
    with st.expander("Show available documents"):
        st.write("Available documents:")
        available_docs = query_available_docs(session)
        st.dataframe([doc["name"] for doc in available_docs])

    # Configure sidebar options and initialize messages
    configure_options()
    initialize_messages()

    # Tabbed Layout for Chat and Emotion Analysis
    tab1, tab2 = st.tabs(["💬 Chat", "📊 Emotion Analysis"])

    # Handle Chat in Tab 1
    with tab1:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Handle user input
        if user_question := st.chat_input("What would you like to discuss today? (E.g., mental health, well-being)"):
            st.session_state.messages.append({"role": "user", "content": user_question})
            with st.chat_message("user"):
                st.markdown(user_question)

            # Show assistant's response with a spinner while generating the answer
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                sanitized_question = user_question.replace("'", "")
                with st.spinner(f"{st.session_state.model_name} thinking..."):
                    response, url_link, relative_path = complete_response(session, sanitized_question, rag)
                    message_placeholder.markdown(response)

                    if rag:
                        st.markdown(f"Link to [{relative_path}]({url_link})")

                    # Optionally display the feedback history for debugging or tracking purposes
                    # st.write("Feedback History:", st.session_state.feedback_history)

                    # if st.radio("Was this response helpful?", ("👍", "👎")) and st.button("Submit Feedback"):
                    #      st.session_state.feedback_history.append({"response": response, "feedback": st.radio})

                # Save the response and emotion analysis in session history
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Analyze emotion and check if CBT should be provided based on threshold
            user_emotion, confidence = analyze_emotion(user_question)
            # st.session_state.messages[-1]["emotion"] = user_emotion
            # st.session_state.messages[-1]["emotion_confidence"] = score
            # st.session_state.emotion_data_changed = True
            st.write(f"**Detected Emotion**: {user_emotion} (Confidence: {confidence:.2f})")
            cbt_suggestion = get_cbt_techniques(user_emotion)
            st.session_state.messages[-1]["cbt"] = cbt_suggestion
            st.write(f"CBT Suggestion: {cbt_suggestion}")

            if 'feedback_history' not in st.session_state:
                st.session_state.feedback_history = []

            feedback = st.radio("Was this response helpful?", ("👍", "👎"))

            # Button to submit the feedback
            if st.button("Submit Feedback"):
                # Append the feedback and response to the session state history
                st.session_state.feedback_history.append({"response": response, "feedback": feedback})
                st.success("Thank you for your feedback!")
            st.session_state.emotion_history.append(user_emotion)

            #
            # # Fallback logic for low confidence or neutral emotion
            # print('score-emotion_threshold',score,emotion_threshold)
            # if score >= emotion_threshold:

            # else:
            #     default_cbt = get_default_cbt()  # Use default if confidence is low or emotion is neutral
            #     st.session_state.messages[-1]["cbt"] = default_cbt
            #     st.write(f"Fallback CBT Suggestion: {default_cbt}")

            # # Save the response and emotion analysis in session history
            # st.session_state.messages.append({"role": "assistant", "content": response})

    # Tab 2: Emotion Analysis and Graphs
    with tab2:
        with st.expander("Emotion Tracking Graph"):
            plot_emotion_distribution(st.session_state.emotion_history)


if __name__ == "__main__":
    main()
