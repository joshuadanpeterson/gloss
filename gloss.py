#!/usr/bin/env python
"""
gloss.py
This script is a command-line interface (CLI) application for a glossary. It uses the click library to handle command-line arguments and options.

The glossary data is imported from `glossary.glossary_data` and `glossary.glossary_help`.
"""


import click
from rich.console import Console
from rich.text import Text
import emoji
from glossary.glossary_data import glossary
from glossary.glossary_help import help_content

console = Console()


def format_term(term, definition):
    icon = emoji.emojize(definition.get("icon", ""), use_aliases=True)
    color = definition.get("color", "white")
    description = definition.get("description", definition)
    alt = ", ".join(definition.get("alt", []))

    term_text = Text(term, style=color)
    icon_text = Text(icon)
    description_text = Text(description)
    alt_text = Text(f" (also: {alt})") if alt else Text("")

    return Text.assemble(icon_text, " ", term_text, ": ", description_text, alt_text)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("term")
def search(term):
    """Search for a term in the glossary."""
    result = {
        key: value for key, value in glossary.items() if term.lower() in key.lower()
    }
    if not result:
        console.print(f"No results found for '{term}'", style="bold red")
    for key, value in result.items():
        formatted_text = format_term(key, value)
        console.print(formatted_text)


@cli.command()
@click.argument("category")
def list(category):
    """List all terms in a specific category."""
    categories = {
        "TODO": ["TODO", "FIX", "HACK", "WARN", "PERF", "NOTE", "TEST", "DEPRECATED"],
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
        "HTTP": [
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
    terms = categories.get(category.upper(), [])
    if not terms:
        console.print(f"No category found for '{category}'", style="bold red")
    all_terms = []
    for term in terms:
        definition = glossary.get(term, {})
        all_terms.append(term)
        if isinstance(definition, dict) and "alt" in definition:
            all_terms.extend(definition["alt"])
    for term in all_terms:
        definition = glossary.get(term, {})
        formatted_text = format_term(term, definition)
        console.print(formatted_text)


@cli.command()
@click.argument("term")
def show(term):
    """Show the definition of a specific term."""
    definition = glossary.get(term.upper(), "Term not found.")
    if definition == "Term not found.":
        console.print(definition, style="bold red")
    else:
        formatted_text = format_term(term.upper(), definition)
        console.print(formatted_text)


@cli.command()
def help():
    """Show the help menu."""
    console.print(help_content, style="green")


if __name__ == "__main__":
    cli()
