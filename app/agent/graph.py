from langgraph.graph import StateGraph, END
from app.agent.workflow import check_requirements_node
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
    "check_requirements",
    check_requirements_node,
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
    "check_requirements",
)

graph_builder.add_edge(
    "check_requirements",
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

def process_request(
    user_input: str,
    previous_state: dict | None = None,
    intent: str | None = None,
):

    if previous_state is None:

        state = {

            "user_input": user_input,

            "intent": intent or "",

            "selected_tool": "",

            "workflow_state": "",

            "collected_information": {},

            "missing_fields": [],

            "pending_confirmation": False,

            "pending_action": "",

            "tool_result": None,

            "response": "",
        }

    else:

        state = previous_state

        state["user_input"] = user_input

    final_state = graph.invoke(state)

    return final_state