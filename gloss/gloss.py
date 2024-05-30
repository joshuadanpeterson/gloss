#!/usr/bin/env python
"""
gloss.py
This script is a command-line interface (CLI) application for a glossary. It uses the click library to handle command-line arguments and options.

The glossary data is imported from `glossary.glossary_data` and `glossary.glossary_help`.
"""


# gloss.py

import click
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.table import Table
import emoji
from .glossary.glossary_data import glossary
from .glossary.glossary_help import help_content
from .glossary.category_dict import categories_dict
from .glossary.category_list import category_list

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
