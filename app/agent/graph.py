from langgraph.graph import StateGraph, END
from app.agent.agent_state import AgentState
from app.agent.nodes import (
    detect_intent_node,
    execute_tool_node,
    save_history_node,
    response_node,
)

graph_builder = StateGraph(AgentState)

graph_builder.add_node(
    "detect_intent",
    detect_intent_node,
)

graph_builder.add_node(
    "execute_tool",
    execute_tool_node,
)

graph_builder.add_node(
    "response",
    response_node,
)

graph_builder.add_node(
    "save_history",
    save_history_node,
)

graph_builder.set_entry_point(
    "detect_intent"
)

graph_builder.add_edge(
    "detect_intent",
    "execute_tool",
)

graph_builder.add_edge(
    "execute_tool",
    "save_history",
)

graph_builder.add_edge(
    "save_history",
    "response",
)

graph_builder.add_edge(
    "response",
    END,
)

graph = graph_builder.compile()

def process_request(user_input: str, intent: str | None = None):

    initial_state = {

        "user_input": user_input,

        "intent": intent or "",

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