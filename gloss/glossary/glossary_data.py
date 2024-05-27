"""
glossary/glossary_data.py
This contains a dictionary of terms and their descriptions.
"""

glossary = {
    "FIX": {
        "description": "Bug that needs to be fixed.",
        "icon": ":bug:",
        "color": "red",
        "alt": ["FIXME", "BUG", "FIXIT", "ISSUE"],
    },
    "TODO": {
        "description": "General task to be completed.",
        "icon": ":white_check_mark:",
        "color": "blue",
    },
    "HACK": {
        "description": "Temporary workaround that should be improved.",
        "icon": ":zap:",
        "color": "yellow",
    },
    "WARN": {
        "description": "Indication of potential issues.",
        "icon": ":warning:",
        "color": "yellow",
        "alt": ["WARNING", "XXX"],
    },
    "PERF": {
        "description": "Performance improvements.",
        "icon": ":rocket:",
        "color": "green",
        "alt": ["OPTIM", "PERFORMANCE", "OPTIMIZE"],
    },
    "NOTE": {
        "description": "Important comment or explanation.",
        "icon": ":memo:",
        "color": "cyan",
        "alt": ["INFO"],
    },
    "TEST": {
        "description": "Test-related annotations.",
        "icon": ":hourglass_flowing_sand:",
        "color": "magenta",
        "alt": ["TESTING", "PASSED", "FAILED"],
    },
    "DEPRECATED": {
        "description": "Marks code that is outdated and will be removed in the future.",
        "icon": ":warning:",
        "color": "grey",
    },
    "feat": "A new feature.",
    "fix": "A bug fix.",
    "docs": "Documentation changes.",
    "style": "Code style changes (e.g., formatting, white-space).",
    "refactor": "Code changes that neither fix a bug nor add a feature.",
    "perf": "Performance improvements.",
    "test": "Adding or correcting tests.",
    "chore": "Routine tasks and maintenance.",
    "improvement": "A change that enhances the existing functionality.",
    "build": "Changes that affect the build system or external dependencies.",
    "ci": "Changes to our CI configuration files and scripts.",
    "revert": "Reverts a previous commit.",
    "200": "OK: The request was successful.",
    "201": "Created: The request was successful and a new resource was created.",
    "202": "Accepted: The request has been accepted for processing, but the processing has not been completed.",
    "204": "No Content: The server successfully processed the request, but is not returning any content.",
    "301": "Moved Permanently: The resource has been permanently moved to a new URL.",
    "302": "Found: The resource has been temporarily moved to a different URL.",
    "304": "Not Modified: The resource has not been modified since the last request.",
    "400": "Bad Request: The server cannot or will not process the request due to client error.",
    "401": "Unauthorized: The client must authenticate itself to get the requested response.",
    "403": "Forbidden: The client does not have access rights to the content.",
    "404": "Not Found: The server cannot find the requested resource.",
    "405": "Method Not Allowed: The request method is known by the server but has been disabled and cannot be used.",
    "500": "Internal Server Error: The server encountered an unexpected condition.",
    "501": "Not Implemented: The server does not support the functionality required to fulfill the request.",
    "502": "Bad Gateway: The server was acting as a gateway or proxy and received an invalid response from the upstream server.",
    "503": "Service Unavailable: The server is not ready to handle the request.",
    "504": "Gateway Timeout: The server was acting as a gateway or proxy and did not receive a timely response from the upstream server.",
    "505": "HTTP Version Not Supported: The HTTP version used in the request is not supported by the server.",
    "506": "Variant Also Negotiates: Transparent content negotiation for the request results in a circular reference.",
    "507": "Insufficient Storage: The server is unable to store the representation needed to complete the request.",
    "508": "Loop Detected: The server detected an infinite loop while processing the request.",
    "510": "Not Extended: Further extensions to the request are required for the server to fulfill it.",
    "511": "Network Authentication Required: The client needs to authenticate to gain network access.",
    "INFO": {
        "description": "Informational messages that highlight the progress of the application.",
        "icon": ":information_source:",
        "color": "cyan",
    },
    "WARN": {
        "description": "Indication of potential issues.",
        "icon": ":warning:",
        "color": "yellow",
        "alt": ["WARNING", "XXX"],
    },
    "ERROR": {
        "description": "Error events that might still allow the application to continue running.",
        "icon": ":x:",
        "color": "red",
    },
    "DEBUG": {
        "description": "Fine-grained informational events that are most useful to debug an application.",
        "icon": ":mag:",
        "color": "blue",
    },
    "FATAL": {
        "description": "Severe error events that will presumably lead the application to abort.",
        "icon": ":skull:",
        "color": "red",
    },
}
