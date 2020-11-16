import time
from messenger import Messenger

if __name__ == '__main__':
    bot = Messenger()
    old = bot.getMessage()
    bot.sendMessage('안녕하세요. 출근했습니다.')
    bot.sendMessage('관심 키워드를 입력하시면\n관련 기사 제목을 보여드립니다.')
    bot.sendMessage('좋은 하루 보내세요.')

    while True:
        new = bot.getMessage()
        if new != old:
            response = bot.searchKeyword(new.get('message'))
            bot.sendMessage(response)
            old = new
        time.sleep(1)

