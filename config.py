from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "29481920"))
API_HASH = environ.get("API_HASH", "f700ddb0930acfab095b00911a2e6f3a")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "8195241636")) # Owner Id or Admin Id

# Give Your Force Join to update Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "https://t.me/Botsxupdate")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://ahaan:ahaad@ahaan.hgkeruq.mongodb.net/?retryWrites=true&w=majority&appName=ahaan")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
