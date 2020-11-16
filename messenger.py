import os
import telegram
from dotenv import load_dotenv
from crawler import Naver

load_dotenv(verbose=True)
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

class Messenger():
    def __init__(self):
        self.bot = telegram.Bot(token=TELEGRAM_API_TOKEN)
        self.updates = self.bot.getUpdates()

    def updateBot(self):
        self.updates = self.bot.getUpdates()
    
    def getMessage(self):
        try:
            response = self.updates[-1]
            return {'first_name': response.message.chat.first_name,
                    'last_name': response.message.chat.last_name,
                    'message': response.message.text}
        except IndexError: # something goes wrong
            return None 
        
    def sendMessage(self, message):
        try:
            chat_id = self.updates[-1].message.chat.id
            self.bot.sendMessage(chat_id=chat_id, text=message)
            print('done')
        except IndexError:
            print('Not available ... please type something on your bot')


    def searchKeyword(self, keyword):
        naver = Naver()
        return naver.get_newspaper(keyword)
    
