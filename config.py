import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))  # take environment variables from .env.


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')
    SERPAPI_API_KEY = os.environ.get('SERPAPI_API_KEY')