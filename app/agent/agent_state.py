from typing import Any
from typing import TypedDict


class AgentState(TypedDict):

    # Current user message
    user_input: str

    # Detected intent
    intent: str

    # Selected tool
    selected_tool: str

    # Current workflow stage
    workflow_state: str

    # Information collected during the conversation
    collected_information: dict[str, Any]

    # Required information still missing
    missing_fields: list[str]

    # Waiting for confirmation?
    pending_confirmation: bool

    # Action waiting to be executed
    pending_action: str
    pending_tool: str

    # Tool execution result
    tool_result: dict | None

    # Final assistant response
    response: str

    # Language
    language: str

    # Last created incident
    last_incident: dict | None

    # Last generated report
    last_report: dict | None

    # Agent reasoning
    reasoning: str
    
    conversation_history: list[dict]