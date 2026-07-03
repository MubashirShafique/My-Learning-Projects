#=====================================  Importing Libraries ===================================

from search_agent import agent
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model=os.getenv('OPENAI_MODEL', 'gpt-4o-mini'))


# Defining the structure output that we want to gent fron the over model 
class Output(BaseModel):
    research_report: str
    urls: list[str]

str_model = model.with_structured_output(Output)


# this is prompt 
report_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research assistant. Your task is to take raw search results "
        "and conversation history and synthesize it into a clean, comprehensive markdown research report.\n\n"
        "Guidelines:\n"
        "1. Write the `research_report` strictly as clean prose using Markdown (headings, bullet points, bold text).\n"
        "2. CRITICAL: Do NOT include any URLs, hyperlinks, or brackets like [Source] or (http...) inside the `research_report` text. It must be pure text.\n"
        "3. Extract all valid source URLs from the raw data and place them exclusively in the `urls` list field.\n"
        "4. Do not invent facts. Only use the provided context.\n"
        "5. Do not include any conversational filler (e.g., 'Here is the report')."
    ),
    (
        "human", 
        "Here is the raw data and search results from the agent:\n\n{agent_output}"
    )
])

# Making chain that work  sequentially it means onece output will be input for other  
research_chain = report_prompt | str_model


#------------------------- This Code is For Testing Purpose ---------------------------------------

# Executing first agent 

# response = agent.invoke(
#     {"messages": [("user", "What are the top news about Pakistan?")]},
#     config={"configurable": {"thread_id": "1"}} 
# )


# takiing its output

# raw_history = ""
# for msg in response['messages']:
   
#     raw_history += f"[{msg.type.upper()}]: {msg.content}\n\n"


# Now Executing the research chain 

# print("Generating structured report...")
# final_response = research_chain.invoke({"agent_output": raw_history})
    

# print("\n--- Markdown Report ---")
# print(final_response.research_report)
    
# print("\n--- Extracted URLs ---")
# print(final_response.urls)