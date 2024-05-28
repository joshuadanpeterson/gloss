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
    # Database
    "SELECT": {
        "description": "SQL command to retrieve data from a database.",
        "icon": "🔍",
        "color": "#1E90FF",  # DodgerBlue
    },
    "INSERT": {
        "description": "SQL command to insert data into a table.",
        "icon": "➕",
        "color": "#32CD32",  # LimeGreen
    },
    "UPDATE": {
        "description": "SQL command to modify existing data in a table.",
        "icon": "✏️",
        "color": "#FFA500",  # Orange
    },
    "DELETE": {
        "description": "SQL command to delete data from a table.",
        "icon": "❌",
        "color": "#FF4500",  # OrangeRed
    },
    "JOIN": {
        "description": "SQL command to combine rows from two or more tables.",
        "icon": "🔗",
        "color": "#6A5ACD",  # SlateBlue
    },
    "INDEX": {
        "description": "SQL command to create an index on a table.",
        "icon": "📑",
        "color": "#FFD700",  # Gold
    },
    "VIEW": {
        "description": "SQL command to create a virtual table based on the result-set of an SQL statement.",
        "icon": "👁️",
        "color": "#00CED1",  # DarkTurquoise
    },
    "TRANSACTION": {
        "description": "SQL command to manage transactions in a database.",
        "icon": "💳",
        "color": "#8B4513",  # SaddleBrown
    },
    # API
    "GET": {
        "description": "HTTP method to request data from a server.",
        "icon": "📥",
        "color": "#1E90FF",  # DodgerBlue
    },
    "POST": {
        "description": "HTTP method to submit data to a server.",
        "icon": "📤",
        "color": "#32CD32",  # LimeGreen
    },
    "PUT": {
        "description": "HTTP method to update data on a server.",
        "icon": "✏️",
        "color": "#FFA500",  # Orange
    },
    "DELETE": {
        "description": "HTTP method to delete data from a server.",
        "icon": "❌",
        "color": "#FF4500",  # OrangeRed
    },
    "PATCH": {
        "description": "HTTP method to apply partial modifications to data on a server.",
        "icon": "🔧",
        "color": "#6A5ACD",  # SlateBlue
    },
    "OPTIONS": {
        "description": "HTTP method to describe the communication options for the target resource.",
        "icon": "⚙️",
        "color": "#FFD700",  # Gold
    },
    "HEAD": {
        "description": "HTTP method to request the headers that would be returned if the specified resource would be requested with a GET method.",
        "icon": "🗂️",
        "color": "#00CED1",  # DarkTurquoise
    },
    # Security
    "XSS": {
        "description": "Cross-site scripting, a type of security vulnerability typically found in web applications.",
        "icon": "🛡️",
        "color": "#FF4500",  # OrangeRed
    },
    "CSRF": {
        "description": "Cross-site request forgery, an attack that forces an end user to execute unwanted actions on a web application in which they are currently authenticated.",
        "icon": "🔒",
        "color": "#32CD32",  # LimeGreen
    },
    "SQL Injection": {
        "description": "A code injection technique that might destroy your database.",
        "icon": "💉",
        "color": "#1E90FF",  # DodgerBlue
    },
    "Encryption": {
        "description": "The process of converting information or data into a code to prevent unauthorized access.",
        "icon": "🔐",
        "color": "#FFD700",  # Gold
    },
    "Decryption": {
        "description": "The process of converting encrypted data back into its original form.",
        "icon": "🔓",
        "color": "#FF4500",  # OrangeRed
    },
    "Hashing": {
        "description": "Transforming data into a fixed-size string of characters, which is typically a hash code.",
        "icon": "🔢",
        "color": "#6A5ACD",  # SlateBlue
    },
    "SSL/TLS": {
        "description": "Protocols for establishing authenticated and encrypted links between networked computers.",
        "icon": "🔗",
        "color": "#00CED1",  # DarkTurquoise
    },
    "Firewall": {
        "description": "A network security system that monitors and controls incoming and outgoing network traffic.",
        "icon": "🔥",
        "color": "#FF4500",  # OrangeRed
    },
    # Networking
    "IP": {
        "description": "Internet Protocol, a set of rules governing the format of data sent over the internet or local network.",
        "icon": "🌐",
        "color": "#1E90FF",  # DodgerBlue
    },
    "TCP": {
        "description": "Transmission Control Protocol, a standard that defines how to establish and maintain a network conversation through which application programs can exchange data.",
        "icon": "🔄",
        "color": "#32CD32",  # LimeGreen
    },
    "UDP": {
        "description": "User Datagram Protocol, an alternative communication protocol to TCP used primarily for establishing low-latency and loss-tolerating connections between applications on the internet.",
        "icon": "📡",
        "color": "#FFA500",  # Orange
    },
    "DNS": {
        "description": "Domain Name System, a hierarchical and decentralized naming system for computers, services, or other resources connected to the internet or a private network.",
        "icon": "🌍",
        "color": "#FFD700",  # Gold
    },
    "HTTP": {
        "description": "Hypertext Transfer Protocol, the foundation of any data exchange on the Web, and it is a protocol used for transmitting hypertext requests and information between servers and browsers.",
        "icon": "📄",
        "color": "#6A5ACD",  # SlateBlue
    },
    "HTTPS": {
        "description": "Hypertext Transfer Protocol Secure, an extension of HTTP used for secure communication over a computer network, and is widely used on the Internet.",
        "icon": "🔒",
        "color": "#00CED1",  # DarkTurquoise
    },
    "FTP": {
        "description": "File Transfer Protocol, a standard network protocol used for the transfer of computer files between a client and server on a computer network.",
        "icon": "📁",
        "color": "#8B4513",  # SaddleBrown
    },
    "SSH": {
        "description": "Secure Shell, a cryptographic network protocol for operating network services securely over an unsecured network.",
        "icon": "🔑",
        "color": "#FF4500",  # OrangeRed
    },
    # Cloud
    "IaaS": {
        "description": "Infrastructure as a Service, a form of cloud computing that provides virtualized computing resources over the internet.",
        "icon": "☁️",
        "color": "#1E90FF",  # DodgerBlue
    },
    "PaaS": {
        "description": "Platform as a Service, a category of cloud computing services that provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the infrastructure.",
        "icon": "🛠️",
        "color": "#32CD32",  # LimeGreen
    },
    "SaaS": {
        "description": "Software as a Service, a software distribution model in which a third-party provider hosts applications and makes them available to customers over the Internet.",
        "icon": "💻",
        "color": "#FFA500",  # Orange
    },
    "Serverless": {
        "description": "A cloud-computing execution model in which the cloud provider runs the server, and dynamically manages the allocation of machine resources.",
        "icon": "🔌",
        "color": "#FFD700",  # Gold
    },
    "Cloud Storage": {
        "description": "A model of computer data storage in which the digital data is stored in logical pools, said to be on 'the cloud'.",
        "icon": "💾",
        "color": "#6A5ACD",  # SlateBlue
    },
    "Virtualization": {
        "description": "The creation of a virtual (rather than actual) version of something, such as an operating system, a server, a storage device, or network resources.",
        "icon": "🖥️",
        "color": "#00CED1",  # DarkTurquoise
    },
    "Kubernetes": {
        "description": "An open-source container-orchestration system for automating computer application deployment, scaling, and management.",
        "icon": "🚢",
        "color": "#8B4513",  # SaddleBrown
    },
    "Docker": {
        "description": "A set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.",
        "icon": "🐳",
        "color": "#1E90FF",  # DodgerBlue
    },
    # DevOps
    "CI/CD": {
        "description": "Continuous Integration and Continuous Deployment, a method to frequently deliver apps to customers by introducing automation into the stages of app development.",
        "icon": "🔄",
        "color": "#1E90FF",  # DodgerBlue
    },
    "Pipeline": {
        "description": "A set of automated processes that allow developers and DevOps professionals to reliably and efficiently compile, build, and deploy their code to their production compute platforms.",
        "icon": "🚀",
        "color": "#32CD32",  # LimeGreen
    },
    "Infrastructure as Code": {
        "description": "The process of managing and provisioning computer data centers through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.",
        "icon": "💻",
        "color": "#FFA500",  # Orange
    },
    "Monitoring": {
        "description": "The process of continuously observing a system's performance and operation.",
        "icon": "📈",
        "color": "#FFD700",  # Gold
    },
    "Logging": {
        "description": "The process of keeping a log, which is a record of events or transactions.",
        "icon": "📝",
        "color": "#6A5ACD",  # SlateBlue
    },
    "Ansible": {
        "description": "An open-source software provisioning, configuration management, and application-deployment tool enabling infrastructure as code.",
        "icon": "🤖",
        "color": "#00CED1",  # DarkTurquoise
    },
    "Terraform": {
        "description": "An open-source infrastructure as code software tool created by HashiCorp.",
        "icon": "🌍",
        "color": "#8B4513",  # SaddleBrown
    },
    "Kubernetes": {
        "description": "An open-source container-orchestration system for automating computer application deployment, scaling, and management.",
        "icon": "🚢",
        "color": "#8B4513",  # SaddleBrown
    },
    # Programming
    "OOP": {
        "description": "Object-Oriented Programming, a programming paradigm based on the concept of 'objects', which are data structures that contain data and code.",
        "icon": "🔲",
        "color": "#1E90FF",  # DodgerBlue
    },
    "Functional Programming": {
        "description": "A programming paradigm where programs are constructed by applying and composing functions.",
        "icon": "🔣",
        "color": "#32CD32",  # LimeGreen
    },
    "Recursion": {
        "description": "The process of defining a problem (or the solution to a problem) in terms of (a simpler version of) itself.",
        "icon": "🔁",
        "color": "#FFA500",  # Orange
    },
    "Polymorphism": {
        "description": "The provision of a single interface to entities of different types.",
        "icon": "🔄",
        "color": "#FFD700",  # Gold
    },
    "Encapsulation": {
        "description": "The bundling of data, along with the methods that operate on that data, into a single unit.",
        "icon": "📦",
        "color": "#6A5ACD",  # SlateBlue
    },
    "Inheritance": {
        "description": "A mechanism where you can derive a class from another class for a hierarchy of classes that share a set of attributes and methods.",
        "icon": "🔗",
        "color": "#00CED1",  # DarkTurquoise
    },
    "Abstraction": {
        "description": "A technique for arranging complexity of computer systems, where a higher-level concept is used to hide the more complex details.",
        "icon": "🔍",
        "color": "#8B4513",  # SaddleBrown
    },
    # Version Control
    "Branch": {
        "description": "A parallel version of a repository that diverges from the main working project.",
        "icon": "🌿",
        "color": "#32CD32",  # LimeGreen
    },
    "Merge": {
        "description": "The process of integrating changes from different branches in a version control system.",
        "icon": "🔀",
        "color": "#FFA500",  # Orange
    },
    "Rebase": {
        "description": "The process of moving or combining a sequence of commits to a new base commit.",
        "icon": "🔃",
        "color": "#1E90FF",  # DodgerBlue
    },
    "Commit": {
        "description": "A record of changes made to a repository.",
        "icon": "📜",
        "color": "#FFD700",  # Gold
    },
    "Pull Request": {
        "description": "A method of submitting contributions to an open development project.",
        "icon": "🔄",
        "color": "#00CED1",  # DarkTurquoise
    },
    "Push": {
        "description": "Sending committed changes to a remote repository.",
        "icon": "📤",
        "color": "#8B4513",  # SaddleBrown
    },
    "Clone": {
        "description": "Creating a local copy of a remote repository.",
        "icon": "🐑",
        "color": "#6A5ACD",  # SlateBlue
    },
    "Fork": {
        "description": "Creating a personal copy of someone else's project.",
        "icon": "🍴",
        "color": "#FF4500",  # OrangeRed
    },
    # Containers
    "Docker": {
        "description": "A set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.",
        "icon": "🐳",
        "color": "#1E90FF",  # DodgerBlue
    },
    "Kubernetes": {
        "description": "An open-source container-orchestration system for automating computer application deployment, scaling, and management.",
        "icon": "🚢",
        "color": "#8B4513",  # SaddleBrown
    },
    "Container": {
        "description": "A standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.",
        "icon": "📦",
        "color": "#32CD32",  # LimeGreen
    },
    "Pod": {
        "description": "A group of one or more containers with shared storage/network, and a specification for how to run the containers.",
        "icon": "📦",
        "color": "#FFD700",  # Gold
    },
    "Service": {
        "description": "An abstract way to expose an application running on a set of Pods as a network service.",
        "icon": "🔌",
        "color": "#FFA500",  # Orange
    },
    "Deployment": {
        "description": "An API object that manages a replicated application, typically by running Pods.",
        "icon": "🚀",
        "color": "#00CED1",  # DarkTurquoise
    },
    "Volume": {
        "description": "A directory, possibly with some data in it, which is accessible to the containers in a Pod.",
        "icon": "💾",
        "color": "#6A5ACD",  # SlateBlue
    },
    "Namespace": {
        "description": "A Kubernetes object that provides a mechanism for isolating groups of resources within a single cluster.",
        "icon": "🌐",
        "color": "#FF4500",  # OrangeRed
    },
    # Testing
    "Unit Test": {
        "description": "A level of software testing where individual units/components of a software are tested.",
        "icon": "🔍",
        "color": "#1E90FF",  # DodgerBlue
    },
    "Integration Test": {
        "description": "A level of software testing where individual units are combined and tested as a group.",
        "icon": "🔗",
        "color": "#32CD32",  # LimeGreen
    },
    "Functional Test": {
        "description": "A type of software testing that validates the software system against the functional requirements/specifications.",
        "icon": "🔧",
        "color": "#FFA500",  # Orange
    },
    "End-to-End Test": {
        "description": "A methodology used to test whether the flow of an application is performing as designed from start to finish.",
        "icon": "🔄",
        "color": "#FFD700",  # Gold
    },
    "TDD": {
        "description": "Test-Driven Development, a software development process relying on software requirements being converted to test cases before software is fully developed.",
        "icon": "📝",
        "color": "#6A5ACD",  # SlateBlue
    },
    "BDD": {
        "description": "Behavior-Driven Development, a software development process that emerged from TDD, where requirements are written in a natural language that non-technical stakeholders can understand.",
        "icon": "📜",
        "color": "#00CED1",  # DarkTurquoise
    },
    "Mocking": {
        "description": "A technique in unit testing where an object mimics the behavior of a real object.",
        "icon": "🎭",
        "color": "#8B4513",  # SaddleBrown
    },
    "Regression Test": {
        "description": "A type of software testing to confirm that a recent program or code change has not adversely affected existing features.",
        "icon": "🔙",
        "color": "#FF4500",  # OrangeRed
    },
    # Bash
    "0": {
        "description": "Success: The command completed successfully.",
        "icon": "✅",
        "color": "#32CD32",  # LimeGreen
    },
    "1": {
        "description": "General Error: A catchall for general errors.",
        "icon": "❗",
        "color": "#FF4500",  # OrangeRed
    },
    "2": {
        "description": "Misuse of Shell Builtins: The command used a shell builtin incorrectly.",
        "icon": "⚠️",
        "color": "#FFD700",  # Gold
    },
    "126": {
        "description": "Command Invoked Cannot Execute: The command is not executable.",
        "icon": "🚫",
        "color": "#FF4500",  # OrangeRed
    },
    "127": {
        "description": "Command Not Found: The command could not be found.",
        "icon": "🔍",
        "color": "#FFA500",  # Orange
    },
    "128": {
        "description": "Invalid Exit Argument: Exit status out of range.",
        "icon": "❓",
        "color": "#1E90FF",  # DodgerBlue
    },
    "129": {
        "description": "Hangup: The command was terminated by a hangup signal (SIGHUP).",
        "icon": "📴",
        "color": "#6A5ACD",  # SlateBlue
    },
    "130": {
        "description": "Terminated: The command was terminated by an interrupt signal (SIGINT).",
        "icon": "🔌",
        "color": "#00CED1",  # DarkTurquoise
    },
    "137": {
        "description": "Killed: The command was terminated by a kill signal (SIGKILL).",
        "icon": "💀",
        "color": "#8B4513",  # SaddleBrown
    },
    "139": {
        "description": "Segmentation Fault: The command caused a segmentation fault (SIGSEGV).",
        "icon": "🧠",
        "color": "#FF4500",  # OrangeRed
    },
    "255": {
        "description": "Exit Status Out of Range: Exit status out of range or not specified.",
        "icon": "❌",
        "color": "#FF4500",  # OrangeRed
    },
}
