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


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    pass


@cli.command()
@click.argument("term")
def search(term):
    """Search for terms containing the specified keyword in the glossary."""
    result = {
        key: value for key, value in glossary.items() if term.lower() in key.lower()
    }
    if not result:
        console.print(f"No results found for '{term}'", style="bold red")
    for key, value in result.items():
        formatted_text = format_term(key, value)
        console.print(formatted_text)


@cli.command()
@click.argument("term")
def show(term):
    """Show the definition of a specific term."""
    term = term.upper()
    definition = glossary.get(term, "Term not found.")
    if definition == "Term not found.":
        console.print(definition, style="bold red")
    else:
        formatted_text = format_term(term, definition)
        console.print(formatted_text)


@cli.command()
@click.argument("category")
def list(category):
    """List all terms in a specific category."""
    categories = {
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
            "SyntaxError",
            "TypeError",
            "ReferenceError",
            "RangeError",
            "IOError",
            "TimeoutError",
        ],
        "log": ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
    }
    category_order = {
        "todo": ["TODO", "NOTE", "TEST", "PERF", "HACK", "FIX", "WARN", "DEPRECATED"],
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
            "SyntaxError",
            "TypeError",
            "ReferenceError",
            "RangeError",
            "IOError",
            "TimeoutError",
        ],
        "log": ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
    }
    category = category.lower()
    terms = categories.get(category, [])
    if not terms:
        console.print(f"No category found for '{category}'", style="bold red")
        return

    ordered_terms = sorted(terms, key=lambda term: category_order[category].index(term))

    for term in ordered_terms:
        definition = glossary.get(term, {})
        formatted_text = format_term(term, definition)
        console.print(formatted_text)


@cli.command()
def categories():
    """List all available categories."""
    table = Table(title="Available Categories")

    table.add_column("Category", justify="left", style="bold blue")
    table.add_column("Description", justify="left", style="bold")

    category_list = [
        ("TODO", "Task annotations such as TODO, FIXME, HACK"),
        (
            "commit",
            "Commit message types such as feat, fix, docs, improvement, build, ci, revert",
        ),
        ("HTTP", "HTTP status codes such as 200, 201, 400, 404, 500"),
        ("errors", "Common error types such as SyntaxError, TypeError"),
        ("log", "Log levels such as DEBUG, INFO, WARN, ERROR, FATAL"),
    ]

    for category, description in category_list:
        table.add_row(category, description)

    console.print(table)


@cli.command()
def help():
    """Show the help menu."""
    console.print(Markdown(help_content))


if __name__ == "__main__":
    cli()
