from app.agent.agent_state import AgentState
from app.agent.router import detect_intent
from app.tools.registry import TOOL_REGISTRY
from app.services.history_service import save_chat

def detect_intent_node(state: AgentState):

    if not state["intent"]:
        state["intent"] = detect_intent(state["user_input"])

    return state

def execute_tool_node(state: AgentState):

    intent = state["intent"]

    tool = TOOL_REGISTRY.get(intent)

    if tool is None:
        state["tool_result"] = {
            "error": "No tool available for this request."
        }
        return state

    state["selected_tool"] = intent
    state["tool_result"] = tool(state["user_input"])

    return state

def response_node(state: AgentState):

    state["response"] = "Completed"

    return state

def save_history_node(state: AgentState):

    save_chat(
        state["user_input"],
        str(state["tool_result"]),
    )

    return state