from app.agent.agent_state import AgentState
from app.agent.router import detect_intent
from app.tools.registry import TOOL_REGISTRY

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