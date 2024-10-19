#(©)t.me/CodeFlix_Bots




import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


load_dotenv()
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22902589"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3045f3e99c422584a2b587e0d9731170")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002410749602"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "New_Saransh_Chahar")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7385295244"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ ᴛʜᴇʀᴇ {first}!\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ʙᴏᴛ\nᴘᴏᴡᴇʀᴇᴅ ʙʏ : @HKB_ANIME\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ\nᴛʜʀᴏᴜɢʜ ᴛʜᴇ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋꜱ ♡")
try:
    ADMINS=[7385295244]
    for x in (os.environ.get("ADMINS", "7385295244").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {first} !⚡\n\n🫧 Pʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴀʟʟ ᴏꜰ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ\n   ɪ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - @HKB_ANIME"

ADMINS.append(OWNER_ID)
ADMINS.append(7385295244)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
