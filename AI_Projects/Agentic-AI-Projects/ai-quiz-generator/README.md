# 🧠 AI Quiz Generator

An AI-powered quiz generation app built with **Streamlit** and **LangChain**, using OpenAI's GPT models to generate multiple choice questions on any topic. After completing the quiz, users can download a PDF report of their results.

---

##  Features

- Generate MCQ quizzes on **any topic** instantly using AI
- Choose from **Easy**, **Medium**, or **Hard** difficulty levels
- Select between **5 to 50 questions** per quiz
- Interactive quiz interface with instant score evaluation
- Download a **PDF report** of your results

---

##  Tech Stack

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Frontend / Web UI |
| [LangChain](https://www.langchain.com/) | LLM integration & structured output |
| [OpenAI GPT](https://openai.com/) | Quiz question generation |
| [Pydantic](https://docs.pydantic.dev/) | Data validation & structured output schema |
| [ReportLab](https://www.reportlab.com/) | PDF report generation |
| [Python Dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📁 Project Structure

```
ai-quiz-generator/
├── app.py                 # Main Streamlit application
├── quiz_generator.py      # LangChain + OpenAI quiz generation logic
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (see setup below)
└── README.md
```

---

##  Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-quiz-generator.git
cd ai-quiz-generator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root of the project:

```bash
touch .env   # macOS/Linux
# OR manually create a .env file on Windows
```

Add the following variables to your `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

> **How to get your OpenAI API Key:**
> 1. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
> 2. Sign in or create an account
> 3. Click **"Create new secret key"**
> 4. Copy the key and paste it as the value of `OPENAI_API_KEY` in your `.env` file

> **Note:** `OPENAI_MODEL` is optional. It defaults to `gpt-4o-mini` if not set. You can change it to `gpt-4o` for higher quality output.

---

## ▶ Running the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

##  How to Use

1. Enter a **topic** in the sidebar (e.g., `Python`, `World War 2`, `Mathematics`)
2. Select a **difficulty level** (Easy / Medium / Hard)
3. Choose the **number of questions** using the slider
4. Click **"Generate Quiz"**
5. Answer all the questions and click **"Submit Answers"**
6. View your score and download the **PDF result report**

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
