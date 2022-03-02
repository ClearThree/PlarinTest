import os


if not os.path.isdir(os.path.join(os.getcwd(), "logs")):
    os.mkdir(os.path.join(os.getcwd(), "logs"))

# MAIN APP CONFIG
APP_TITLE = os.environ.get("APP_TITLE", "Plarin test case")
APP_DESCRIPTION = """
## Info:
- [**GitHub**](https://github.com/ClearThree/plarintest)
"""
APP_HOST = os.environ.get("APP_HOST", "127.0.0.1")
APP_PORT = int(os.environ.get("APP_PORT", 8000))
APP_LOG_LEVEL = os.environ.get("APP_LOG_LEVEL", "info")
APP_LOG_FILE_NAME = os.environ.get("APP_LOG_FILE_NAME", "plarin.log")
APP_SECRET_TOKEN = os.environ.get("APP_SECRET_TOKEN", "very_secret_token")

# CORSMiddleware
ALLOWED_ORIGINS = ["*"]
ALLOWED_CREDENTIALS = True
ALLOWED_METHODS = ["*"]
ALLOWED_HEADERS = ["*"]

# POSTGRES
MONGO_USER = os.environ.get("MONGO_USER", "clearthree")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "plarinpassword")
MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
MONGO_DB = os.environ.get("MONGO_DB", "plarin")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION", "plarin")
DATABASE_URL = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
