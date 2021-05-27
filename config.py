import os
from dotenv import load_dotenv
import datetime

load_dotenv()


BASEDIR = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    DEBUG = True
    TESTING = False
    
    MONGODB_URI = os.getenv("MONGODB_URI")

    SECRET_KEY = os.getenv("SECRET_KEY")
    PROPAGATE_EXCEPTIONS = True  # bubble propagation

    SESSION_COOKIE_SECURE = False


