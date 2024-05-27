"""
glossary/glossary_data.py
This contains a dictionary of terms and their descriptions.
"""

glossary = {
    "FIX": {
        "description": "Bug that needs to be fixed. (See also FIXME, BUG, FIXIT, ISSUE)",
        "icon": "🐛",
        "color": "#FF0000",  # red
    },
    "TODO": {
        "description": "General task to be completed.",
        "icon": "✅",
        "color": "#0000FF",  # blue
    },
    "HACK": {
        "description": "Temporary workaround that should be improved.",
        "icon": "🛠️",
        "color": "#FFFF00",  # yellow
    },
    "WARN": {
        "description": "Indication of potential issues. (See also WARNING, XXX)",
        "icon": "⚠️",
        "color": "#FFA500",  # orange
    },
    "PERF": {
        "description": "Performance improvements. (See also OPTIM, PERFORMANCE, OPTIMIZE)",
        "icon": "🚀",
        "color": "#00FF00",  # green
    },
    "NOTE": {
        "description": "Important comment or explanation. (See also INFO)",
        "icon": "📝",
        "color": "#00FFFF",  # cyan
    },
    "TEST": {
        "description": "Test-related annotations. (See also TESTING, PASSED, FAILED)",
        "icon": "🧪",
        "color": "#FF00FF",  # magenta
        "alt": [],
    },
    "DEPRECATED": {
        "description": "Marks code that is outdated and will be removed in the future.",
        "icon": "⚠️",
        "color": "#808080",  # grey
    },
    "feat": {
        "description": "A new feature.",
        "icon": "✨",
        "color": "#00FFFF",  # cyan
    },
    "fix": {
        "description": "A bug fix.",
        "icon": "🐛",
        "color": "#00FFFF",  # cyan
    },
    "docs": {
        "description": "Documentation changes.",
        "icon": "📝",
        "color": "#00FFFF",  # cyan
    },
    "style": {
        "description": "Code style changes (e.g., formatting, white-space).",
        "icon": "💄",
        "color": "#00FFFF",  # cyan
    },
    "refactor": {
        "description": "Code changes that neither fix a bug nor add a feature.",
        "icon": "♻️",
        "color": "#00FFFF",  # cyan
    },
    "perf": {
        "description": "Performance improvements.",
        "icon": "⚡",
        "color": "#00FFFF",  # cyan
    },
    "test": {
        "description": "Adding or correcting tests.",
        "icon": "✅",
        "color": "#00FFFF",  # cyan
    },
    "chore": {
        "description": "Routine tasks and maintenance.",
        "icon": "🔧",
        "color": "#00FFFF",  # cyan
    },
    "improvement": {
        "description": "A change that enhances the existing functionality.",
        "icon": "✨",
        "color": "#00FFFF",  # cyan
    },
    "build": {
        "description": "Changes that affect the build system or external dependencies.",
        "icon": "🏗️",
        "color": "#00FFFF",  # cyan
    },
    "ci": {
        "description": "Changes to our CI configuration files and scripts.",
        "icon": "👷",
        "color": "#00FFFF",  # cyan
    },
    "revert": {
        "description": "Reverts a previous commit.",
        "icon": "⏪",
        "color": "#00FFFF",  # cyan
    },
    "100": {
        "description": "Continue: The server has received the request headers and the client should proceed to send the request body.",
        "color": "#ADD8E6",  # light blue
    },
    "101": {
        "description": "Switching Protocols: The requester has asked the server to switch protocols and the server is acknowledging that it will do so.",
        "color": "#ADD8E6",  # light blue
    },
    "200": {
        "description": "OK: The request was successful.",
        "color": "#00FF00",  # green
    },
    "201": {
        "description": "Created: The request was successful and a new resource was created.",
        "color": "#00FF00",  # green
    },
    "202": {
        "description": "Accepted: The request has been accepted for processing, but the processing has not been completed.",
        "color": "#00FF00",  # green
    },
    "204": {
        "description": "No Content: The server successfully processed the request, but is not returning any content.",
        "color": "#00FF00",  # green
    },
    "301": {
        "description": "Moved Permanently: The resource has been permanently moved to a new URL.",
        "color": "#FFFF00",  # yellow
    },
    "302": {
        "description": "Found: The resource has been temporarily moved to a different URL.",
        "color": "#FFFF00",  # yellow
    },
    "304": {
        "description": "Not Modified: The resource has not been modified since the last request.",
        "color": "#FFFF00",  # yellow
    },
    "400": {
        "description": "Bad Request: The server cannot or will not process the request due to client error.",
        "color": "#FFA500",  # orange
    },
    "401": {
        "description": "Unauthorized: The client must authenticate itself to get the requested response.",
        "color": "#FFA500",  # orange
    },
    "403": {
        "description": "Forbidden: The client does not have access rights to the content.",
        "color": "#FFA500",  # orange
    },
    "404": {
        "description": "Not Found: The server cannot find the requested resource.",
        "color": "#FFA500",  # orange
    },
    "405": {
        "description": "Method Not Allowed: The request method is known by the server but has been disabled and cannot be used.",
        "color": "#FFA500",  # orange
    },
    "500": {
        "description": "Internal Server Error: The server encountered an unexpected condition.",
        "color": "#FF0000",  # red
    },
    "501": {
        "description": "Not Implemented: The server does not support the functionality required to fulfill the request.",
        "color": "#FF0000",  # red
    },
    "502": {
        "description": "Bad Gateway: The server was acting as a gateway or proxy and received an invalid response from the upstream server.",
        "color": "#FF0000",  # red
    },
    "503": {
        "description": "Service Unavailable: The server is not ready to handle the request.",
        "color": "#FF0000",  # red
    },
    "504": {
        "description": "Gateway Timeout: The server was acting as a gateway or proxy and did not receive a timely response from the upstream server.",
        "color": "#FF0000",  # red
    },
    "505": {
        "description": "HTTP Version Not Supported: The HTTP version used in the request is not supported by the server.",
        "color": "#FF0000",  # red
    },
    "506": {
        "description": "Variant Also Negotiates: Transparent content negotiation for the request results in a circular reference.",
        "color": "#FF0000",  # red
    },
    "507": {
        "description": "Insufficient Storage: The server is unable to store the representation needed to complete the request.",
        "color": "#FF0000",  # red
    },
    "508": {
        "description": "Loop Detected: The server detected an infinite loop while processing the request.",
        "color": "#FF0000",  # red
    },
    "510": {
        "description": "Not Extended: Further extensions to the request are required for the server to fulfill it.",
        "color": "#FF0000",  # red
    },
    "511": {
        "description": "Network Authentication Required: The client needs to authenticate to gain network access.",
        "color": "#FF0000",  # red
    },
    "INFO": {
        "description": "Informational messages that highlight the progress of the application.",
        "icon": "ℹ️",
        "color": "#00FFFF",  # cyan
    },
    "ERROR": {
        "description": "Error events that might still allow the application to continue running.",
        "icon": "❌",
        "color": "#FF0000",  # red
    },
    "DEBUG": {
        "description": "Fine-grained informational events that are most useful to debug an application.",
        "icon": "🔍",
        "color": "#0000FF",  # blue
    },
    "FATAL": {
        "description": "Severe error events that will presumably lead the application to abort.",
        "icon": "💀",
        "color": "#FF0000",  # red
    },
    "SyntaxError": {
        "description": "Raised when the parser encounters a syntax error.",
        "color": "#FF0000",  # red
    },
    "TypeError": {
        "description": "Raised when an operation or function is applied to an object of inappropriate type.",
        "color": "#FFA500",  # orange
    },
    "ReferenceError": {
        "description": "Raised when a weak reference proxy is used to access a garbage collected referent.",
        "color": "#FFA500",  # orange
    },
    "RangeError": {
        "description": "Raised when a numeric value is out of range.",
        "color": "#FFA500",  # orange
    },
    "IOError": {
        "description": "Raised when an I/O operation fails.",
        "color": "#FFA500",  # orange
    },
    "TimeoutError": {
        "description": "Raised when a system function timed out at the system level.",
        "color": "#FFA500",  # orange
    },
}
