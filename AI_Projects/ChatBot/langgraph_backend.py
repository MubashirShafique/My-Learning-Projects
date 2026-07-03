from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import sqlite3




load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    max_tokens=250
)


class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]



def chat_node(state:State):
    messages=state['messages']
    response = llm.invoke(messages)
    return {'messages':[response]}


conn=sqlite3.connect(database='chatbot_database.db',check_same_thread=False)

# checkpoint 
checkpointer=SqliteSaver(conn=conn)

graph=StateGraph(State)

graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)


def retrive_all_threads():
    all_threads=set()
    for state in checkpointer.list(None):
        all_threads.add(state.config['configurable']['thread_id'])


    return list(all_threads)