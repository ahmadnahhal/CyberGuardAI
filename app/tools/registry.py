from app.tools.password_tool import execute as password_tool
from app.tools.phishing_tool import execute as phishing_tool
from app.tools.information_tool import execute as information_tool
from app.tools.report_tool import execute as report_tool
from app.tools.incident_tool import execute as incident_tool
from app.tools.memory_tool import execute as execute


TOOL_REGISTRY = {
    "password": password_tool,
    "phishing": phishing_tool,
    "information": information_tool,
    "report": report_tool,
    "incident": incident_tool,
    "memory": execute,
}