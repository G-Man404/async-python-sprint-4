import os
from pydantic import BaseSettings, PostgresDsn
from logging import config as logging_config

from src.core.logger import LOGGING

logging_config.dictConfig(LOGGING)

PROJECT_NAME = os.getenv('PROJECT_NAME', 'Link Shortener')
PROJECT_HOST = os.getenv('PROJECT_HOST', '0.0.0.0')
PROJECT_PORT = int(os.getenv('PROJECT_PORT', '8000'))


class AppSettings(BaseSettings):
    app_title: str = "Link Shortener"
    database_dsn: PostgresDsn = "postgresql+asyncpg://postgres:postgres@localhost:5432/collection"

    class Config:
        env_file = '.env'


app_settings = AppSettings()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
