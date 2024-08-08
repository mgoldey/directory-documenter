import os


def scrape_directory(directory):
    file_data = []
    for root, _, files in os.walk(directory):
        # ignore .venv
        if ".venv" in root:
            continue
        for file in files:
            if file.endswith(".md") or file.endswith(".py") or file.endswith(".toml"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    file_content = f.read()
                file_data.append(f"### {file_path}\n{file_content}")
    return file_data
