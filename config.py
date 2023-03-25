from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("5926297757:AAHXHx-FMkpg16_ShWykWadi1ZfaZ3Hr7ys")
API_ID = int(getenv("API_ID", "2013655"))
API_HASH = getenv("036e4559f48a51ef4e33b2d6a1e7f502")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "90"))
ASSISTANT_PREFIX = list(getenv("", "/").split())
MONGO_DB_URI = getenv("mongodb+srv://Patuska:Ismet@patuska.vjubctv.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1300527267").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5026921065").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001811271788"))
MUSIC_BOT_NAME = getenv("Patuska")
#HEROKU_API_KEY = getenv("HEROKU_API_KEY")
#HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/ArapSikenGenc/maho"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("1ApWapzMBu4gzcWt7wBJRxLC5ESqVD3GkPpABDhuPETwm0Wsv_l-2CkjjYXXV6LALFS4uF4NINjWsF2dWJOPHs_BhIwbsaSBo_z4gOsCbwIt_8FumLROxKvj3d-2fP0t_24N7X3tadSdLiqqufzetU4TI0OszsCPnZz4IYeVNXwSmH7y1CEEXdNVtxyi2YTgSqwsss9QI2qPNXnRdPK5PwQSFGf0HZY2aX-VvW8EyQBjuxjfdKjWkR8Bv0z4zv3IjLT7OmYaGkRuv8mTJeRl4M5ZSUUea2o7v5j_EdRNx9uNueYdGE-fH8p0GettZsCQRuJTDRja4a98EG7IAz8R1XooY0mi_wG0=")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
