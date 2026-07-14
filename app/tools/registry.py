from app.tools.password_tool import execute as password_tool
from app.tools.information_tool import execute as information_tool
from app.tools.phishing_tool import execute as phishing_tool

TOOL_REGISTRY = {
    "password": password_tool,
}

TOOL_REGISTRY = {
    "password": password_tool,
    "information": information_tool,
}

TOOL_REGISTRY = {

    "password": password_tool,

    "information": information_tool,

    "phishing": phishing_tool,
}