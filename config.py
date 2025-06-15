import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "20288951"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "e8cb5fb7a475b5f5eb3b0ef0e6ca03a8")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7833842279").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "KAKA 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
