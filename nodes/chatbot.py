from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from graph.graph_builder import graph_builder, State
from langgraph.graph import START, END

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

def chatbot(state:State): 
    try:
        return {"messages": [llm.invoke(state["messages"])]}
    except Exception as e:
        print(f"An error occurred: {e}")
        

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except:
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break