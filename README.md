# Directory Documenter

## Overview

Directory Documenter is a Python tool designed to generate comprehensive documentation for a directory of code files automatically. By leveraging the power of OpenAI's GPT-4 API, this service analyzes the contents of specified files within a directory and constructs a detailed README file. This tool is particularly useful for developers and teams who want to maintain up-to-date documentation without manual overhead.

## Features

- **Automated Documentation Generation**: Automatically create a README file based on the content of your Python (`.py`), Markdown (`.md`), and TOML (`.toml`) files.
- **Integration with OpenAI **: Utilizes Azure-hosted GPT-4 models to generate high-quality documentation.
- **Customizable Prompts**: Uses a predefined prompt template to ensure consistent and accurate documentation.

## Usage

To install Directory Documenter, you need to have Python installed (>=3.10).

1. Install `directory-documenter` via pip
    ```bash
    pip install git+https://github.com/mgoldey/directory-documenter.git
    ```

This stores `document_directory` and `analyze_directory` as runnable scripts in your python environment.

2. Run the tool:
    ```bash
    document_directory "${directory_path}"
    ```

This command will scrape the directory (excluding any `.venv` directories) and generate a `README.md` file at the root of your project.

## Project Structure

The project consists of the following main files:

- `pyproject.toml`: Configuration file for `poetry` containing project metadata and dependencies.
- `document_directory.py`: Main script that handles directory scraping, prompt construction, and interaction with the GPT-4 API.
- `analyze_directory.py`: Script similar to `document_directory.py` but geared towards generating an architectural advice document.
- `directory_documenter/file_utils.py`: Utility functions for scraping directory contents.
- `directory_documenter/config.py`: Configuration settings management using pydantic.

## Configuration

The script assumes that the OpenAI API key is set in the environment and uses a specific Azure endpoint. Ensure you have the following environment variables set:

- `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint.
- `AZURE_DEPLOYMENT`: Your Azure OpenAI deployment name.
- `OPENAI_API_KEY`: Your OpenAI API key.


You can set these variables in your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export AZURE_OPENAI_ENDPOINT="https://your-azure-endpoint.openai.azure.com/"
export AZURE_DEPLOYMENT='gpt4o'
export OPENAI_API_KEY="your_openai_api_key"
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Be sure to follow the existing code style and include relevant tests.

## Contact

For any questions or issues, please open an issue on GitHub or contact Matthew Goldey at matthew.goldey@gmail.com.

---

Thank you for using Directory Documenter! We hope it makes maintaining your project documentation easier and more efficient.

