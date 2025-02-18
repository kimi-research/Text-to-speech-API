import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Load settings from envs
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instantiate Setting object
settings = Settings()
