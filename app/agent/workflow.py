from app.agent.agent_state import AgentState


def check_requirements_node(
    state: AgentState,
) -> AgentState:
    """
    Current version:
    Always allow execution.

    Multi-turn collection will be implemented later.
    """

    state["workflow_state"] = "ready"
    state["missing_fields"] = []

    return state