import os

class Config:
    API_ID = int(os.environ.get("API_ID", "25114508")) #Karışmayın
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce") #Karışmayın
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7161888538:AAHCMcV5CCgxcYx1nUfgT2TqvpFD9-sjIMA") #Botunuzun Tokenini Girin .  
