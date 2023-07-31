from os import getenv
from dotenv import load_dotenv

load_dotenv()

FLASK_APP = getenv("FLASK_APP") or "main"
FLASK_ENV = getenv("FLASK_ENV") or "development"
FLASK_HOST = getenv("FLASK_HOST") or "127.0.0.1"
FLASK_PORT = int(getenv("FLASK_PORT")) or 5000
