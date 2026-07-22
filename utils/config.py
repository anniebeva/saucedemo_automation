import os

from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")