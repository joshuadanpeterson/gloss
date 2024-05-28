#!/usr/bin/env python
"""
gloss.py
This script is a command-line interface (CLI) application for a glossary. It uses the click library to handle command-line arguments and options.

The glossary data is imported from `glossary.glossary_data` and `glossary.glossary_help`.
"""


import click
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.table import Table
import emoji
from .glossary.glossary_data import glossary
from .glossary.glossary_help import help_content

console = Console()


def format_term(term, definition):
    if isinstance(definition, dict):
        icon = emoji.emojize(definition.get("icon", ""))
        color = definition.get("color", "white")
        description = definition.get("description", "")
    else:
        icon = ""
        color = "white"
        description = definition

    term_text = Text(term, style=color)
    icon_text = Text(icon)
    description_text = Text(description)

    return Text.assemble(icon_text, " ", term_text, ": ", description_text)


categories_dict = {
    "todo": ["TODO", "FIX", "HACK", "WARN", "PERF", "NOTE", "TEST", "DEPRECATED"],
    "commits": [
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
        "429",
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
}

category_list = [
    ("TODO", "Task annotations such as TODO, FIXME, HACK"),
    (
        "commits",
        "Commit message types such as feat, fix, docs, improvement, build, ci, revert",
    ),
    ("HTTP", "HTTP status codes such as 200, 201, 400, 404, 500"),
    (
        "errors",
        "Common error types such as AssertionError, AttributeError, SyntaxError, TypeError, and more.",
    ),
    ("log", "Log levels such as DEBUG, INFO, WARN, ERROR, FATAL"),
    ("database", "Database operations and SQL commands"),
    ("api", "API methods and status codes"),
    ("security", "Security practices and vulnerabilities"),
    ("networking", "Networking protocols and configurations"),
    ("cloud", "Cloud computing services and architectures"),
    ("devops", "DevOps practices and tools"),
    ("programming", "Programming concepts and paradigms"),
    ("version_control", "Version control terms and commands"),
    ("containers", "Containerization and orchestration"),
    ("testing", "Software testing methodologies and tools"),
    ("bash", "Common Bash error codes and their meanings"),
]


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    pass


@cli.command()
@click.argument("term")
def search(term):
    """Search for terms with an exact match in the glossary."""
    term = term.upper() if term.isupper() else term.lower()
    result = {key: value for key, value in glossary.items() if key.lower() == term}
    if not result:
        console.print(f"No results found for '{term}'", style="bold red")
    else:
        for key, value in result.items():
            # Determine the category of the term
            category = next(
                (cat for cat, terms in categories_dict.items() if key in terms),
                "Unknown Category",
            )
            formatted_text = format_term(key, value)
            console.print(f"Category: {category}")
            console.print(formatted_text)


@cli.command()
@click.argument("category")
def list(category):
    """List all terms in a specific category."""
    category = category.lower()
    terms = categories_dict.get(category, [])
    if not terms:
        console.print(f"No category found for '{category}'", style="bold red")
        return

    for term in terms:
        definition = glossary.get(term, {})
        formatted_text = format_term(term, definition)
        console.print(formatted_text)


@cli.command()
def categories():
    """List all available categories."""
    table = Table(title="Available Categories")

    table.add_column("Category", justify="left", style="bold cyan")
    table.add_column("Description", justify="left", style="bold green")

    for category, description in category_list:
        table.add_row(category, description)

    console.print(table)


@cli.command()
def help():
    """Show the help menu."""
    console.print(Markdown(help_content))


if __name__ == "__main__":
    cli()
