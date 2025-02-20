from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from graph.graph_builder import graph_builder, State

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

def chatbot(state:State): 
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)