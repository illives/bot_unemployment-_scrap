from Threads_resources.threads_resources import MyThread

from main_unemployment import main_unemployment_crawler
from main_population import main_population_crawler



if __name__=='__main__':

    crawler_unemployment = MyThread(main_unemployment_crawler)
    crawler_unemployment.start()

    crawler_population = MyThread(main_population_crawler)
    crawler_population.start()

    while crawler_population.is_alive() and crawler_unemployment.is_alive():
        pass

    print('Execução do Crawler Terminada!')