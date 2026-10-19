from langgraph.graph import StateGraph, START, END
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-120b')

class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage],add_messages]

def chat_node(state: ChatState):

    messages = state['messages']

    response = llm.invoke(messages)

    return {'messages':[response]}

checkpointer = MemorySaver()

graph = StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)

thread_id = '1'
while True:
    user_message = input('Type here: ')

    if user_message in ['exit','bye','quit']:
        break

    config = {'configurable': {'thread_id': thread_id}}
    llm_response = chatbot.invoke({'messages':[HumanMessage(content=user_message)]}, config=config)

    print('AI: ', llm_response['messages'][-1].content)