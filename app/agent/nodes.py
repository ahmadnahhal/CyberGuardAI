from app.agent.agent_state import AgentState
from app.agent.router import detect_intent
from app.tools.registry import TOOL_REGISTRY
from app.services.history_service import save_chat
from app.services.log_service import log_execution
from app.services.translation_service import tr

def detect_intent_node(state: AgentState):

    if not state["intent"]:
        state["intent"] = detect_intent(state["user_input"])
        state["workflow_state"] = "intent_detected"

    return state

def execute_tool_node(state: AgentState):

    # Stop if we still need information
    if state["workflow_state"] == "waiting_for_information":

        missing = state["missing_fields"][0]

        questions = {
            "password": "Please enter the password you would like me to analyze.",
            "title": "What is the incident title?",
            "severity": "What severity should I assign? (Low, Medium, High, Critical)",
        }

        state["response"] = questions.get(
            missing,
            f"Please provide: {missing}"
        )

        return state

    intent = state["intent"]

    tool = TOOL_REGISTRY.get(intent)

    if tool is None:

        state["tool_result"] = {
            "status": "error",
            "tool": None,
            "data": None,
            "error": "No tool available for this request."
        }

        return state

    # Don't execute until confirmation has been given
    if state["workflow_state"] != "ready":
         return state

    state["selected_tool"] = intent

    if intent in (
    "information",
    "incident",
    "report",
    ):

     state["tool_result"] = tool(
        state["user_input"],
        state.get("conversation_history", []),
    )

    else:

     state["tool_result"] = tool(
        state["user_input"],
     )

    return state

def response_node(state: AgentState):

    result = state.get("tool_result")

    # No tool executed (confirmation, cancellation, etc.)
    if result is None:
        return state

    if result["status"] == "error":

        state["response"] = f"❌ {result['error']}"
        state["workflow_state"] = "completed"

        return state

    tool = result["tool"]
    data = result["data"]

    if tool == "password":

     recommendations = data.get("recommendations", [])

     if "generated_password" in data:

        message = (
            "## 🔐 Generated Password\n\n"
            f"**Password:** `{data['generated_password']}`\n\n"
            f"**Strength:** {data['strength']}\n\n"
            f"**Score:** {data['score']}/10\n\n"
            f"**Entropy:** {data['entropy']} bits\n\n"
            f"**Estimated Crack Time:** {data['crack_time']}"
        )

     else:

        message = (
            "## 🔑 Password Analysis\n\n"
            f"**Strength:** {data['strength']}\n\n"
            f"**Score:** {data['score']}/10\n\n"
            f"**Entropy:** {data['entropy']} bits\n\n"
            f"**Estimated Crack Time:** {data['crack_time']}"
        )

     if recommendations:

        message += "\n\n### Recommendations"

        for recommendation in recommendations:
            message += f"\n• {recommendation}"

     state["response"] = message

    elif tool == "phishing":

        message = (
            f"## 📧 Phishing Analysis\n\n"
            f"**Risk:** {data['risk']}\n\n"
            f"**Risk Score:** {data['score']}"
        )

        findings = data.get("findings", [])

        if findings:

            message += "\n\n### Indicators"

            for finding in findings:
                message += f"\n• {finding}"

        state["response"] = message

    elif tool == "information":

        state["response"] = data["answer"]

    elif tool == "incident":

        state["response"] = (
            f"{tr('incident_created', state['language'])}\n\n"
            f"**Incident ID:** {data['incident_id']}\n"
            f"**Title:** {data['title']}\n"
            f"**Severity:** {data['severity']}\n"
            f"**Status:** {data['status']}"
        )

    elif tool == "report":

        state["response"] = (
            f"{tr('report_created', state['language'])}\n\n"
            f"**Report ID:** {data['report_id']}\n"
            f"**Title:** {data['title']}\n"
            f"**Type:** {data['report_type']}\n\n"
            f"The report has been saved to the database."
        )
        
    elif tool == "memory":

        state["response"] = data["message"]

    else:

        state["response"] = f"Unknown tool: {tool}"

    state["workflow_state"] = "completed"
    
    status = "Success"

    if result["status"] == "error":
     status = "Error"

    log_execution(
     intent=state["intent"],
     selected_tool=state["selected_tool"],
     status=status,
     message=state["response"],
     )
    
    history = state.get("conversation_history", [])

    history.append(
     {
        "user": state["user_input"],
        "assistant": state["response"],
     }
    )

# Keep only the last 6 exchanges
    state["conversation_history"] = history[-6:]

    return state

def save_history_node(state: AgentState):

    save_chat(
        state["user_input"],
        str(state["tool_result"]),
    )

    return state