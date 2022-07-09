from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import logging
import os


class Report:

    def __init__(self):
        self.final_report = None
        self.url = None
        self._homedir = os.getcwd()[:-7]
        self.webdriver = None
        self.html_content = None
        self.soup = None
        self.table = None

    def create_final_report(self):
        self.final_report = pd.read_html(str(self.table))[0]

    def save_final_report(self):
        self.final_report.to_excel(f'{self._homedir}\\report\\final_report.xlsx', index = False)


class WebDriver(Report):

    def get_webdriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.webdriver = webdriver.Chrome(f'{self._homedir}\\driver\\chromedriver.exe', chrome_options=options)

    def set_webdriver(self):
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(30)
        self.webdriver.set_page_load_timeout(220)

    def open_urlsite(self):
        self.webdriver.get('https://pt.tradingeconomics.com/country-list/employment-rate')

    def set_tableelement(self):
        element = self.webdriver.find_element('xpath','/html/body/form/div[6]/div/div[1]/div')
        self.html_content = element.get_attribute('outerHTML')
    
    def close_webtabs(self):
        self.webdriver.quit()


class Crawler(WebDriver):
    def instace_htmlparser(self):
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def get_pagetable(self):
        self.table = self.soup.find(name = 'table')


class Process(Crawler):
    pass