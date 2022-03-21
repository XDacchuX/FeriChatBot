from os import environ

ENV = True # make it false for heroku

# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages

if not ENV:
  bot_token = ""
  ARQ_API_KEY = ""
  LANGUAGE = "id"
  api_id = ""
  api_hash = ""
  ARQ_API_BASE_URL = "https://thearq.tech"
  BOT_USERNAME = "Kittu_Robot"
  KONTOL = "Feri"
  MEMEK = "https://telegra.ph/file/4ebf97569f757accc4b36.jpg"
else:
  bot_token = str(environ.get("BOT_TOKEN", None))
  ARQ_API_KEY = str(environ.get("ARQ_API_KEY", None))
  LANGUAGE = str(environ.get("LANGUAGE", "id"))
  api_id = int(environ.get("API_ID", 6))
  api_hash = str(environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e"))
  ARQ_API_BASE_URL = "https://grambuilders.tech"
  BOT_USERNAME = str(environ.get("BOT_USERNAME", "Kittu_Robot"))
  KONTOL = str(environ.get("BOT_NAME", "Feri"))
  MEMEK = str(environ.get("MEDIA", "https://telegra.ph/file/4ebf97569f757accc4b36.jpg"))
