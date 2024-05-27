# Importing necessary modules from setuptools package
from setuptools import setup, find_packages

setup(
    name="gloss",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "rich",
        "emoji",
    ],
    entry_points={
        "console_scripts": [
            "gloss=gloss:cli",
        ],
    },
    author="Josh Peterson",
    author_email="joshuadanpeterson@gmail.com",
    description="A CLI tool that provides quick access to a glossary of developer terms, HTTP status codes, log levels, and more.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joshuadanpeterson/gloss",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
