# categories_dict.py


categories_dict = {
    "todo": ["TODO", "FIX", "HACK", "WARN", "PERF", "NOTE", "TEST", "DEPRECATED"],
    "commit": [
        "feat",
        "fix",
        "docs",
        "style",
        "refactor",
        "perf",
        "test",
        "chore",
        "improvement",
        "build",
        "ci",
        "revert",
    ],
    "http": [
        "100",
        "101",
        "200",
        "201",
        "202",
        "204",
        "301",
        "302",
        "304",
        "400",
        "401",
        "403",
        "404",
        "405",
        "429",
        "500",
        "501",
        "502",
        "503",
        "504",
        "505",
        "506",
        "507",
        "508",
        "510",
        "511",
    ],
    "errors": [
        "AssertionError",
        "AttributeError",
        "EOFError",
        "FloatingPointError",
        "ImportError",
        "IndentationError",
        "IndexError",
        "IOError",
        "KeyError",
        "MemoryError",
        "NameError",
        "OverflowError",
        "RangeError",
        "ReferenceError",
        "RuntimeError",
        "SyntaxError",
        "TimeoutError",
        "TypeError",
        "ValueError",
        "ZeroDivisionError",
    ],
    "log": ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
    "database": [
        "SELECT",
        "INSERT",
        "UPDATE",
        "DELETE",
        "JOIN",
        "INDEX",
        "VIEW",
        "TRANSACTION",
    ],
    "api": ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"],
    "security": [
        "XSS",
        "CSRF",
        "SQL Injection",
        "Encryption",
        "Decryption",
        "Hashing",
        "SSL/TLS",
        "Firewall",
    ],
    "networking": ["IP", "TCP", "UDP", "DNS", "HTTP", "HTTPS", "FTP", "SSH"],
    "cloud": [
        "IaaS",
        "PaaS",
        "SaaS",
        "Serverless",
        "Cloud Storage",
        "Virtualization",
        "Kubernetes",
        "Docker",
    ],
    "devops": [
        "CI/CD",
        "Pipeline",
        "Infrastructure as Code",
        "Monitoring",
        "Logging",
        "Ansible",
        "Terraform",
        "Kubernetes",
    ],
    "programming": [
        "OOP",
        "Functional Programming",
        "Recursion",
        "Polymorphism",
        "Encapsulation",
        "Inheritance",
        "Abstraction",
    ],
    "version_control": [
        "Branch",
        "Merge",
        "Rebase",
        "Commit",
        "Pull Request",
        "Push",
        "Clone",
        "Fork",
    ],
    "containers": [
        "Docker",
        "Kubernetes",
        "Container",
        "Pod",
        "Service",
        "Deployment",
        "Volume",
        "Namespace",
    ],
    "testing": [
        "Unit Test",
        "Integration Test",
        "Functional Test",
        "End-to-End Test",
        "TDD",
        "BDD",
        "Mocking",
        "Regression Test",
    ],
    "bash": ["0", "1", "2", "126", "127", "128", "129", "130", "137", "139", "255"],
    "google_apps_script": [
        "TypeError: Cannot read property 'X' of undefined",
        "ReferenceError: X is not defined",
        "SyntaxError: Unexpected token X",
        "QuotaExceededError: Script has exceeded the maximum execution time",
        "RangeError: Maximum call stack size exceeded",
        "Exception: Service invoked too many times in a short time: X",
        "Exception: Cannot call method 'X' of null",
    ],
    "github_labels": [
        "bug",
        "documentation",
        "duplicate",
        "enhancement",
        "good first issue",
        "help wanted",
        "invalid",
        "question",
        "wontfix",
    ],
}
