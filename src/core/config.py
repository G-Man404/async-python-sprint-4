import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn, Field
from logging import config as logging_config
from src.core.logger import LOGGING

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

logging_config.dictConfig(LOGGING)

db_echo_mode = True


class AppSettings(BaseSettings):
    app_title: str = "Title"
    database_dsn: PostgresDsn
    project_name: str = 'Some project name'
    redis_host: str = ...
    redis_port: int = ...
    elastic_host: str = Field(..., env='ELASTIC_HOST_NAME')
    elastic_port: int = Field(9200, env='ELASTIC_PORT')


class Config:
    env_file = '.env'


app_settings = AppSettings()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
