from app.agent.agent_state import AgentState
from app.llm.groq_client import ask_groq


SYSTEM_PROMPT = """
You are CyberGuard AI.

You are a cybersecurity analyst.

Before any tool is executed, analyze the user's request.

Your job is to think, not answer.

Determine:

- What the user wants.
- Important cybersecurity entities.
- Incident type if present.
- Threat category.
- Estimated severity.
- Whether important information is missing.

Respond in short professional notes.

Do not answer the user directly.
"""


def reasoning_node(state: AgentState):

    prompt = f"""
User request:

{state['user_input']}
"""

    reasoning = ask_groq(
        SYSTEM_PROMPT,
        prompt,
    )

    state["reasoning"] = reasoning

    return state