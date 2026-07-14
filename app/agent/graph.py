from langgraph.graph import StateGraph, END
from app.agent.agent_state import AgentState
from app.agent.router import detect_intent
from app.tools.password_tool import execute as password_tool


def detect_intent_node(state: AgentState):

    state["intent"] = detect_intent(state["user_input"])

    return state

def password_node(state: AgentState):

    state["selected_tool"] = "password_tool"

    state["tool_result"] = password_tool(
        state["user_input"]
    )

    return state

def response_node(state: AgentState):

    state["response"] = "Completed"

    return state

graph_builder = StateGraph(AgentState)

graph_builder.add_node(
    "detect_intent",
    detect_intent_node,
)

graph_builder.add_node(
    "password",
    password_node,
)

graph_builder.add_node(
    "response",
    response_node,
)

graph_builder.set_entry_point(
    "detect_intent"
)

graph_builder.add_edge(
    "detect_intent",
    "password",
)

graph_builder.add_edge(
    "password",
    "response",
)

graph_builder.add_edge(
    "response",
    END,
)

graph = graph_builder.compile()

def process_request(user_input: str):

    initial_state = {

        "user_input": user_input,

        "intent": "",

        "selected_tool": "",

        "tool_result": None,

        "response": "",
    }
    
    final_state = graph.invoke(initial_state)

    return {
        "intent": final_state["intent"],
        "result": final_state["tool_result"],
        "response": final_state["response"],
    }