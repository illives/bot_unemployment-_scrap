from crawler_unemployment_resources.resources import Process

def main_unemployment_crawler():
    bot = Process()
    bot.get_webdriver()
    bot.set_webdriver()
    bot.open_urlsite()
    bot.set_tableelement()
    bot.instace_htmlparser()
    bot.get_pagetable()
    bot.create_final_report()
    bot.save_final_report()
   
