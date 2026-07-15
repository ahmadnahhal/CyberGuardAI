from app.agent.agent_state import AgentState


def continue_workflow_node(
    state: AgentState,
) -> AgentState:
    """
    Continue an unfinished workflow.
    """

    if state["workflow_state"] != "waiting_for_information":
        return state

    if not state["missing_fields"]:
        return state

    field = state["missing_fields"][0]

    state["collected_information"][field] = state["user_input"]

    state["missing_fields"].pop(0)

    if state["missing_fields"]:
        return state

    state["workflow_state"] = "ready"

    return state