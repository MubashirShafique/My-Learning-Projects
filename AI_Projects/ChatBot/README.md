# ChatBot

A simple AI chatbot built with **LangGraph**, **LangChain**, and **Streamlit**, featuring persistent conversation history using SQLite checkpointing.

## Features

- Real-time streaming responses from OpenAI's `gpt-4o-mini` model
- Persistent chat history across sessions (stored in SQLite)
- Multiple conversation threads with sidebar navigation
- Start new chats anytime via "New Chat" button

## Project Structure

```
chatbot/
├── langgraph_backend.py    # LangGraph state graph, LLM node, SQLite checkpointer
├── streamlit_frontend.py   # Streamlit UI (chat interface, sidebar, threads)
├── chatbot_database.db     # SQLite database (auto-created on first run)
├── .env                     # API keys (not committed to version control)
```

## Setup

### 1. Clone / copy the project files

### 2. Install dependencies

```bash
pip install streamlit langgraph langchain-openai langchain-core python-dotenv
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY="your-openai-api-key-here"
```


Optional (for LangSmith tracing/observability):

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT='https://api.smith.langchain.com'
LANGCHAIN_API_KEY="your-langsmith-api-key"
LANGCHAIN_PROJECT='chatbot_observability'
```

### 4. Run the app

```bash
streamlit run streamlit_frontend.py
```

## How It Works

- **Backend (`langgraph_backend.py`)**: Defines a LangGraph `StateGraph` with a single node (`chat_node`) that sends messages to the LLM and returns the response. Conversation state is persisted using `SqliteSaver`.
- **Frontend (`streamlit_frontend.py`)**: Provides a chat UI where users can send messages, view streaming responses, and switch between previous conversation threads stored in the sidebar.

## Notes

- The database files (`.db`, `.db-shm`, `.db-wal`) store conversation checkpoints and will be created automatically when the app runs.
- If you regenerate your API keys, update the `.env` file accordingly.
