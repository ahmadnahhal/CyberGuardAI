from typing import TypedDict, Any


class AgentState(TypedDict):
    """
    Shared state passed between LangGraph nodes.
    """

    user_input: str
    intent: str
    selected_tool: str
    tool_result: Any
    confirmation_required: bool
    response: str