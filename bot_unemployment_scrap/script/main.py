from resources.resources import Process

def main():
    bot = Process()
    bot.get_webdriver()
    bot.set_webdriver()
    bot.open_urlsite()
    bot.set_tableelement()
    bot.instace_htmlparser()
    bot.get_pagetable()
    bot.create_final_report()
    bot.save_final_report()
   

if __name__== '__main__':
    main()