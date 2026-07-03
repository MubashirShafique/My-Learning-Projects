# 📝 Autonomous AI Research Assistant

An AI-powered research assistant that searches the web, synthesizes the findings into a clean Markdown report, and lets you download the result as a polished PDF — all through a simple Streamlit interface.

## How It Works

The project has three components that work together:

1. **`search_agent.py`** — The research engine. Built with **LangGraph**, this agent uses the **Tavily Search API** as a tool to browse the web and gather information based on the user's query. It maintains conversation state using an in-memory checkpointer.

2. **`final_report_generator_agent.py`** — The report writer. It takes the raw conversation/search history produced by the search agent and uses an LLM with **structured output** (via Pydantic) to generate:
   - `research_report`: a clean Markdown research report (no inline links/URLs)
   - `urls`: a separate list of all source URLs extracted from the research

3. **`frontend.py`** — The user interface. Built with **Streamlit**, it ties everything together:
   - Takes a research topic/question from the user
   - Runs the search agent and report generator
   - Displays the report and sources in the browser
   - Converts the Markdown report into a downloadable **PDF** using ReportLab

## Project Structure

```
.
├── search_agent.py                    # LangGraph search agent (Tavily tool)
├── final_report_generator_agent.py    # Structured report generation chain
├── frontend.py                        # Streamlit app (entry point)
├── .env                                # Your API keys (you create this)
└── README.md
```

## Requirements

- Python 3.10+
- An [OpenAI API key](https://platform.openai.com/api-keys)
- A [Tavily API key](https://tavily.com/) (free tier available)

## Installation

1. **Clone or download the project files** into a single folder (all three `.py` files must be in the same directory, since they import from each other).

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required libraries**:
   ```bash
   pip install streamlit langchain langchain-openai langchain-tavily langgraph python-dotenv pydantic reportlab
   ```

   Or save this as `requirements.txt` and run `pip install -r requirements.txt`:
   ```
   streamlit
   langchain
   langchain-openai
   langchain-tavily
   langgraph
   python-dotenv
   pydantic
   reportlab
   ```

4. **Create a `.env` file** in the project folder with your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```
   `OPENAI_MODEL` is optional — it defaults to `gpt-4o-mini` if not set.

## Running the App

Launch the Streamlit frontend (this is the only file you run directly):

```bash
streamlit run frontend.py
```

This will open the app in your browser at `http://localhost:8501`.

## Usage

1. Enter a research topic or question in the text box (e.g., *"Latest tech trends in Pakistan"*).
2. Click **Generate Report**.
3. Wait while the agent searches the web and compiles the data.
4. View the generated Markdown report and sources directly in the app.
5. Click **Download PDF Report** to save a formatted PDF copy.

## Notes

- `search_agent.py` contains a commented-out test block at the bottom — safe to leave as is.
- `final_report_generator_agent.py` currently runs a test query ("What are the top news about Pakistan?") automatically when imported. If you don't want this test call to run every time the frontend starts, consider wrapping it in `if __name__ == "__main__":` so it only runs when the file is executed directly.
- Each Streamlit session uses a fixed `thread_id` ("streamlit_session"), so conversation memory is shared across reruns within that session.

## Tech Stack

| Component | Technology |
|---|---|
| Agent orchestration | LangGraph |
| LLM | OpenAI (via LangChain) |
| Web search | Tavily Search API |
| Structured output | Pydantic |
| Frontend | Streamlit |
| PDF generation | ReportLab |
