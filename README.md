# Directory Documenter

## Overview

Directory Documenter is a Python tool designed to generate comprehensive documentation for a directory of code files automatically. By leveraging the power of OpenAI's GPT-4 API, this service analyzes the contents of specified files within a directory and constructs a detailed README file. This tool is particularly useful for developers and teams who want to maintain up-to-date documentation without manual overhead.

## Features

- **Automated Documentation Generation**: Automatically create a README file based on the content of your Python (`.py`), Markdown (`.md`), and TOML (`.toml`) files.
- **Integration with OpenAI GPT-4**: Utilizes the Azure-hosted GPT-4 model to generate high-quality documentation.
- **Customizable Prompts**: Uses a predefined prompt template to ensure consistent and accurate documentation.

## Installation

To install Directory Documenter, you need to have Python installed (version 3.10 or 3.11). It's recommended to use `poetry` for managing dependencies.

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/directory-documenter.git
    cd directory-documenter
    ```

2. Install dependencies using `poetry`:
    ```bash
    poetry install
    ```

## Usage

Directory Documenter is designed to be easy to use through the command line.

1. Navigate to the directory containing your project:
    ```bash
    cd /path/to/your/project
    ```

2. Run the tool:
    ```bash
    python /path/to/directory-documenter/document_directory.py .
    ```

This command will scrape the current directory (excluding any `.venv` directories) and generate a `README.md` file at the root of your project.

## Project Structure

The project consists of the following main files:

- `pyproject.toml`: Configuration file for `poetry` containing project metadata and dependencies.
- `document_directory.py`: Main script that handles directory scraping, prompt construction, and interaction with the GPT-4 API.
- `analyze_directory.py`: Script similar to `document_directory.py` but geared towards generating an architectural advice document.

## Configuration

The script assumes that the OpenAI API key is set in the environment and uses a specific Azure endpoint. Ensure you have the following environment variables set:

- `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint.
- `OPENAI_API_KEY`: Your OpenAI API key.

You can set these variables in your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export AZURE_OPENAI_ENDPOINT="https://your-azure-endpoint.openai.azure.com/"
export OPENAI_API_KEY="your_openai_api_key"
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Be sure to follow the existing code style and include relevant tests.

## Contact

For any questions or issues, please open an issue on GitHub or contact Matthew Goldey at matthew.goldey@gmail.com.

---

Thank you for using Directory Documenter! We hope it makes maintaining your project documentation easier and more efficient.
