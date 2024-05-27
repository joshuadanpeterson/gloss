"""
glossary/glossary_help.py
This file contains the help messages for the glossary CLI tool.
"""

help_content = """
# Gloss CLI - A glossary tool for developers

## Usage:
  `gloss search [TERM]`    Search for a term in the glossary
  `gloss list [CATEGORY]`  List all terms in a specific category
  `gloss show [TERM]`      Show the definition of a specific term

## Categories:
  **TODO**: Task annotations such as :white_check_mark: TODO, :bug: FIX, :zap: HACK
  **commit**: Commit message types such as feat, fix, docs, improvement, build, ci, revert
  **HTTP**: HTTP status codes such as 200, 201, 400, 404, 500
  **errors**: Common error types such as SyntaxError, TypeError
  **log**: Log levels such as DEBUG, INFO, WARN, ERROR, FATAL

## Examples:
  `gloss search TODO`
  `gloss list HTTP`
  `gloss show 404`
"""
