from app.agent.agent_state import AgentState
from app.services.translation_service import tr

CONFIRMATION_INTENTS = {
    "incident",
    "report",
}


def check_requirements_node(
    state: AgentState,
) -> AgentState:

    # -------------------------------
    # Waiting for confirmation
    # -------------------------------
    if state.get("pending_confirmation", False):

        answer = state["user_input"].strip().lower()

        if answer in ("yes", "y", "confirm", "oui", "o"):

            state["pending_confirmation"] = False

            state["intent"] = state["pending_tool"]

            state["pending_tool"] = ""
            
            state["user_input"] = state["pending_action"]

            state["pending_action"] = ""

            state["workflow_state"] = "ready"

            return state

        if answer in ("no", "n", "cancel", "non"):

            state["pending_confirmation"] = False
            state["pending_tool"] = ""

            state["workflow_state"] = "completed"

            state["response"] = tr(
             "operation_cancelled",
             state["language"],
             )

            return state

        state["workflow_state"] = "completed"

        state["response"] = tr(
         "yes_no",
          state["language"],
          )

        return state

    # -------------------------------
    # Require confirmation
    # -------------------------------
    if state["intent"] in CONFIRMATION_INTENTS:

        state["pending_confirmation"] = True

        state["pending_tool"] = state["intent"]
        
        state["pending_action"] = state["user_input"]

        state["workflow_state"] = "waiting_confirmation"

        if state["intent"] == "incident":

            if state["language"] == "french":

               state["response"] = (
               "Je vais créer un nouvel incident.\n\n"
            "Voulez-vous continuer ? (Oui/Non)"
            )

            else:

               state["response"] = (
               "I am ready to create a new incident.\n\n"
               "Do you want to continue? (Yes/No)"
               )
               
        else:

            if state["language"] == "french":

               state["response"] = (
               "Je vais générer et enregistrer un rapport.\n\n"
               "Voulez-vous continuer ? (Oui/Non)"
               )

            else:

              state["response"] = (
               "I am about to generate and save a report.\n\n"
               "Do you want to continue? (Yes/No)"
               )
              
        return state

    # -------------------------------
    # Execute immediately
    # -------------------------------
    state["workflow_state"] = "ready"
    state["missing_fields"] = []

    return state