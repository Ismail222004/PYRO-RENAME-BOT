import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "18942141")

API_HASH = os.environ.get("API_HASH", "76d94bbb29cd80f86b6db9cc835d7f94")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5746427612:AAG9HNwKIjiloddMashTO3jKtuXtkLcBxj0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/MD_NETWORK") 

DB_NAME = os.environ.get("DB_NAME","my")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://minetwork.wyvbnud.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/1283821f19752c9187019.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get('PORT', '8080')
