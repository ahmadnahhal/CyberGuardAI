from app.agent.agent_state import AgentState


def check_requirements_node(
    state: AgentState,
) -> AgentState:
    """
    Determine whether enough information has been collected
    before executing a tool.
    """

    intent = state["intent"]

    state["workflow_state"] = "ready"
    state["missing_fields"] = []

    if intent == "password":

        password = state["user_input"].strip()

        if (
            " " in password
            or len(password) < 4
        ):
            state["workflow_state"] = "waiting_for_information"
            state["missing_fields"] = ["password"]

    elif intent == "incident":

        info = state["collected_information"]

        if "title" not in info:
            state["workflow_state"] = "waiting_for_information"
            state["missing_fields"] = ["title"]

        elif "severity" not in info:
            state["workflow_state"] = "waiting_for_information"
            state["missing_fields"] = ["severity"]

    return state