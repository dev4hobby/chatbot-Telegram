from messenger import Messenger

if __name__ == '__main__':
    my_bot = Messenger()
    result = my_bot.searchKeyword('독감')
    my_bot.sendMessage(result)
