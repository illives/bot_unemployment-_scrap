from genericpath import isfile
import unittest
from selenium import webdriver
import os

class test_WebDriver(unittest.TestCase):

    def setUp(self):
        self.webdriver = webdriver.Chrome(f'{os.getcwd()}\\driver\\chromedriver.exe')
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(30)
        self.webdriver.set_page_load_timeout(220)
        

    def test_if_chromedriver_file_is_in_directory(self):
        print(f'{os.getcwd()}\\driver\\chromedriver.exe')
        assert isfile (f'{os.getcwd()}\\driver\\chromedriver.exe')

    def test_if_url_site_is_avaliable(self):
        self.webdriver.get('https://pt.tradingeconomics.com/country-list/population')
        assert True
 
    def tearDown(self):
        self.webdriver.close()


if __name__=='__main__':
    unittest.main(verbosity=2)
        
