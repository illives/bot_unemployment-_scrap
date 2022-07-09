from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import logging
import os


class Report:

    def __init__(self):
        self.final_report = []
        self.url = None
        self._homedir = os.getcwd()[:-7]
        self.webdriver = None


class WebDriver(Report):

    def get_webdriver(self):
        self.webdriver = webdriver.Chrome(f'{self._homedir}\\driver\\chromedriver.exe')

    def set_webdriver(self):
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(30)
        self.webdriver.set_page_load_timeout(220)

    def open_urlsite(self):
        self.webdriver.get('https://pt.tradingeconomics.com/country-list/employment-rate')

    def click_tabselectio(self):
        pass

class Crawler(WebDriver):
    pass

class Process(Crawler):
    pass