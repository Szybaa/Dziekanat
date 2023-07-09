from dotenv import load_dotenv
import os


class BaseConfig():
    load_dotenv()
    # db_config
    SECRET_KEY = os.getenv('SECRET_KEY')

    