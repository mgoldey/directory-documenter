from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    azure_endpoint: str
    openai_api_key: str
    openai_api_version: str = "2023-03-15-preview"
    azure_deployment: str

    # case insensitive
    class Config:
        case_sensitive = False


# use .env if it exists
settings = Settings()
