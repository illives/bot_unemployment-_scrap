from resources.resources import Process

def main():
    bot = Process()
    bot.get_webdriver()
    bot.set_webdriver()
    bot.open_urlsite()
    input()
   

if __name__== '__main__':
    main()