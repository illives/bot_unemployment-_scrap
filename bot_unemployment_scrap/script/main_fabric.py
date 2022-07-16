from ast import main
from threading import Thread

from main_unemployment import main_unemployment_crawler
from main_population import main_population_crawler


class MyThread(Thread):

    def __init__(self, scrypt):
        self.scrypt = scrypt
        Thread.__init__(self)

    def run(self):
        self.scrypt()


if __name__=='__main__':

    crawler_unemployment = MyThread(main_unemployment_crawler)
    crawler_unemployment.start()

    crawler_population = MyThread(main_population_crawler)
    crawler_population.start()

   