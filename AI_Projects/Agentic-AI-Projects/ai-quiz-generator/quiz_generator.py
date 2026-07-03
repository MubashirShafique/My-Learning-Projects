from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

class MCQ(BaseModel):
    question: str
    options: List[str]
    correct_answer: str

class Quiz(BaseModel):
    quiz_questions: List[MCQ]

model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

llm = ChatOpenAI(
    model=model,
    temperature=0.3
)

structured_llm = llm.with_structured_output(Quiz)


def generate_quiz(topic: str, num_questions: int, difficulty: str):


    prompt = f"""
    Generate {num_questions} multiple choice questions about {topic}.
    The difficulty level of the quiz must be {difficulty}.

    Rules:
    - Exactly 4 options per question
    - Only one correct answer
    - Questions should not repeat
    - Return valid structured output
    """

    response = structured_llm.invoke(prompt)

    return response