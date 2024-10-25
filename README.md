# MindMate Chat Assistant - Leveraging AI for Enhancing Urban Health 
This application is a chatbot built with Streamlit that integrates **Snowflake Cortex** for generating responses and **Cognitive Behavioral Therapy (CBT)**  The app offers a dynamic and interactive UI to enhance the user experience.

## Features

- **Snowflake Cortex Integration**: Query Snowflake LLM for response generation.
- **Document Querying**: Option to retrieve relevant document chunks from Snowflake storage.
- **Interactive UI**: Tabs, checkboxes, and expanders for a clean and dynamic user interface.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/emotion-aware-chat-assistant.git
    cd emotion-aware-chat-assistant
    ```

2. **Install dependencies**:
    Ensure you have Python 3.7 or later installed. Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Snowflake**:
    Create a `properties.ini` file in the root directory with your Snowflake credentials:
    ```ini
    [Snowflake]
    account = <your_account>
    user = <your_user>
    password = <your_password>
    role = <your_role>
    warehouse = <your_warehouse>
    database = <your_database>
    schema = <your_schema>
    ```

4. **Run the app**:
    Start the Streamlit app by running:
    ```bash
    streamlit run app.py
    ```

5. **Access the app**:
    Open your browser and navigate to `http://localhost:8501` to interact with the chatbot.

## Usage

- **Chat with the Assistant**: Type your questions or topics (e.g., mental health, well-being) and the chatbot will respond.
- **Emotion Analysis**: The chatbot detects emotions in user input and provides appropriate CBT techniques based on the confidence level.
- **Dynamic Layout**: Use tabs to view chat history or analyze your emotions over time.
- **Document Search**: Enable document retrieval via Snowflake for context-aware responses (toggle "Use your own documents as context?" in the sidebar).

## Configuration Options

- **Remember Chat History**: Option to retain previous conversation context for enhanced response accuracy.
- **Debug Mode**: Enable debug mode to view summaries of chat history and queries generated for document searches.

## Project Structure

```bash
.
├── app.py                      # Main application file
├── helpers
│   ├── snowflake_helper.py      # Snowflake connection and query helpers
│   ├── chat_helper.py           # Chat state and configuration utilities
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── properties.ini               # Snowflake configuration file (user-provided)
