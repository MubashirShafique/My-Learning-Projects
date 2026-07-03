import streamlit as st
from langgraph_tool_backend import chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage 
import uuid


#******************************** Utility Functions ************************
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id


def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []


def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']

#**************** session Setup *****************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

add_thread(st.session_state['thread_id'])

#************************ Side Bar UI ************************
st.sidebar.title("Langgraph Chatbot")
if st.sidebar.button('new chat'):
    reset_chat()
st.sidebar.header('My conversion')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role': role, 'content': msg.content})
        st.session_state['message_history'] = temp_messages


# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
    
    # Assistant message handling with filter logic
    with st.chat_message('assistant'):
        
        # Generator function jo sirf LLM (chat_node) ka output filter karega
        def filter_ai_stream():
            for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            ):
                # Sirf tab text yield hoga jab chunk 'chat_node' se aa raha ho
                if metadata.get('langgraph_node') == 'chat_node':
                    yield message_chunk.content

        # Streamlit generator ko run karega aur clean output dikhayega
        ai_message = st.write_stream(filter_ai_stream())

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})