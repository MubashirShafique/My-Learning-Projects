# simple_langgraph_ai_agent

A simple AI agent built with **LangGraph**, **LangChain**, and **Streamlit**. 
It can chat normally and also use tools: web search, stock price lookup, and a calculator. 
Chat history is saved in a local SQLite database (`chatbot.db`), so old conversations can be reloaded from the sidebar.

## Project Files

```
simple_langgraph_ai_agent/
├── streamlit_frontend.py     -> Streamlit UI (chat interface, sidebar with chat history)
├── langgraph_tool_backend.py      -> LangGraph agent logic, tools, and SQLite checkpointer
├── chatbot.db      -> SQLite database (auto-created, stores chat threads)
├── .env            -> API keys (DO NOT share this file)
└── README.md
```

## Requirements

Make sure you have Python 3.9 or higher installed.

## Install Required Libraries

Run this single command to install everything needed:

```bash
pip install streamlit langgraph langchain langchain-openai langchain-community python-dotenv duckduckgo-search requests
```

## Setup `.env` File

Create a file named `.env` in the project folder and add your keys:

```
OPENAI_API_KEY="your-openai-api-key-here"
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="your-langsmith-api-key-here"
LANGCHAIN_PROJECT="chatbot_observability_tools"
```


## How to Run

1. Open a terminal in the project folder.
2. Run the Streamlit app:

```bash
streamlit run frontend.py
```

3. Your browser will open automatically at `http://localhost:8501`.

## Features

- **Chat with AI** - Powered by OpenAI's GPT model through LangChain.
- **Web Search Tool** - Uses DuckDuckGo to search the internet for current information.
- **Stock Price Tool** - Fetches live stock prices using Alpha Vantage API.
- **Calculator Tool** - Performs basic math (add, subtract, multiply, divide).
- **Chat History** - All conversations are saved in `chatbot.db` and can be reopened from the sidebar.
- **New Chat** - Click "new chat" in the sidebar to start a fresh conversation thread.

## Notes

- The `chatbot.db` file is created automatically the first time you run the app. You don't need to create it manually.
- The stock price tool currently uses a hardcoded Alpha Vantage API key inside `backend.py`. For better security, move it into `.env` as well.