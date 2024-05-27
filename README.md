# Gloss

Gloss is a Command Line Interface (CLI) tool that acts as a glossary for developers. It helps you quickly look up definitions for various programming terms, HTTP status codes, log levels, and more.

## Features

- **Search**: Quickly search for terms in the glossary.
- **List**: List all terms in a specific category.
- **Show**: Show the definition of a specific term.
- **Help**: Display a help menu with usage instructions and examples.

## Installation

You can install Gloss via pip. Make sure you have Python 3.6 or higher installed.

```sh
pip install gloss
```

## Usage

After installing, you can use the `gloss` command in your terminal.

### Commands

#### Search for a Term

Search for a term in the glossary.

```sh
gloss search [TERM]
```

Example:

```sh
gloss search TODO
```

#### List Terms in a Category

List all terms in a specific category.

```sh
gloss list [CATEGORY]
```

Example:

```sh
gloss list HTTP
```

#### Show the Definition of a Term

Show the definition of a specific term.

```sh
gloss show [TERM]
```

Example:

```sh
gloss show 404
```

#### Display Help Menu

Show the help menu with usage instructions and examples.

```sh
gloss help
```

## Categories

- **TODO**: Task annotations such as TODO, FIXME, HACK
- **commit**: Commit message types such as feat, fix, docs
- **HTTP**: HTTP status codes such as 200, 404, 500
- **errors**: Common error types such as SyntaxError, TypeError
- **log**: Log levels such as DEBUG, INFO, WARN, ERROR, FATAL

## Examples

```sh
# Search for TODO
gloss search TODO

# List all HTTP status codes
gloss list HTTP

# Show the definition of HTTP 404 status code
gloss show 404

# Display help menu
gloss help
```

## Contributing

Contributions are welcome! If you have suggestions for new terms or improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Josh Peterson - [joshuadanpeterson@gmail.com](mailto:joshuadanpeterson@gmail.com)

## Project URL

[https://github.com/joshuadanpeterson/gloss](https://github.com/joshuadanpeterson/gloss)

````

### Steps to Create the README

1. **Create the `README.md` file** in the root of your project directory:
    ```sh
    touch README.md
    ```

2. **Copy and paste the content** above into the `README.md` file.

### Final Directory Structure

Your project directory should look like this:

````

my-project/
├── gloss-env/
├── glossary/
│ ├── **init**.py
│ ├── glossary_data.py
│ └── glossary_help.py
├── gloss.py
├── setup.py
├── MANIFEST.in
├── requirements.txt
└── README.md

```

```
