import os
from dotenv import load_dotenv
load_dotenv()

class Credentials:
    LOGIN = os.getenv("AQA_LOGIN")  # Используем имя переменной из .env
    PASSWORD = os.getenv("AQA_PASSWORD")  # Используем имя переменной из .env