#!/usr/bin/env python3


from fire import Fire
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

from .config import settings
from .file_utils import scrape_directory

openai_llm = AzureChatOpenAI(
    openai_api_version=settings.openai_api_version,
    azure_deployment=settings.azure_deployment,
    azure_endpoint=settings.azure_endpoint,
    openai_api_key=settings.openai_api_key,
)

# Define a template for the prompt
prompt_template = """You are an expert documentation writer. Based on the following files' content, generate a README.md file and other relevant documentation.

Please analyze the code and provide a detailed description of:
1. What the service does
2. How it can be used
3. The overall structure of the project
4. Any other relevant documentation

Files:
{file_contents}

README in Markdown:
"""

# Create the prompt template
prompt = PromptTemplate(template=prompt_template, input_variables=["file_contents"])
chain = prompt | openai_llm


def generate_documentation(file_contents):
    # Join the file contents into a single string
    joined_contents = "\n\n".join(file_contents)
    # Run the LLM chain to generate the README
    result = chain.invoke(joined_contents)
    return result.content


def main(directory_to_scrape):
    # Scrape the directory
    file_contents = scrape_directory(directory_to_scrape)

    # Generate the documentation
    documentation = generate_documentation(file_contents)

    # Save the generated documentation to a file
    with open(f"{directory_to_scrape}/README.md", "w", encoding="utf-8") as f:
        f.write(documentation)

    print("Documentation generated successfully!")


def cli():
    Fire(main)


if __name__ == "__main__":
    cli()
