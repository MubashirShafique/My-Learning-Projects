#--------------------- Importing all Libraries ------------------------------
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START
from langgraph.checkpoint.memory import InMemorySaver
from langchain_tavily import TavilySearch
from langchain_tavily import TavilySearch 
from pydantic import BaseModel, HttpUrl
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from typing import TypedDict, Annotated
import os

load_dotenv()

# taking model name from .env 
model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# LLM Instance
llm = ChatOpenAI(model=model_name)

#  Tools Setup
tavily_tool = TavilySearch(max_results=5) 
tools_list = [tavily_tool]


model_with_tools = llm.bind_tools(tools_list)

tool_node = ToolNode(tools_list)


class State(TypedDict):
    messages: Annotated[list, add_messages]

# 6. Chatbot Function
def chatbot(state: State):
    return {"messages": [model_with_tools.invoke(state["messages"])]}



# Making Grpah 
graph = StateGraph(State)

graph.add_node('chatbot', chatbot)
graph.add_node('tools', tool_node)

graph.add_edge(START, 'chatbot')
graph.add_conditional_edges("chatbot", tools_condition)
graph.add_edge('tools', 'chatbot')

# compiling the Grpah 
agent = graph.compile(checkpointer=InMemorySaver())




#======================= Testing ===========================


# response = agent.invoke(
#     {"messages": [("user", "What are the top news about Pakistan?")]},
#     config={"configurable": {"thread_id": "1"}} 
# )


# print(response['messages'][-1].content)