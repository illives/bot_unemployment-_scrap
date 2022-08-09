from selenium import webdriver
from bs4 import BeautifulSoup
from page.page_elements import *
from time import sleep
import pandas as pd
import logging
import os

logger = logging
logger.basicConfig(filename='app.log',format='%(asctime)s - %(message)s', level=logging.INFO)

logger.info('Unemployment_Crawler-Iniciando uso de Recursos')
class Report:

    def __init__(self):
        self.final_report = None
        self.url = None
        self._homedir = os.getcwd()
        self.webdriver = None
        self.html_content = None
        self.soup = None
        self.table = None

    def create_final_report(self):
        try:
            self.final_report = pd.read_html(str(self.table))[0]
            logger.info('Unemployment_Crawler-Criando Relatorio Final')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Erro ao Criar Relatorio: %s', erro)


    def save_final_report(self):
        try:
            self.final_report.to_excel(f'{self._homedir}\\report\\unemployment_final_report.xlsx', index = False)
            logger.info('Unemployment_Crawler-Salvando Relatorio Final unemployment.')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Erro ao Salvar Relatorio: %s', erro)


class WebDriver(Report):

    def get_webdriver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            self.webdriver = webdriver.Chrome(f'{self._homedir}\\driver\\chromedriver.exe', chrome_options=options)
            logger.info('Unemployment_Crawler-WEBDRIVE iniciado.')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Erro ao iniciar o WEBDRIVER:  %s', erro)


    def set_webdriver(self):
        try:
            self.webdriver.maximize_window()
            self.webdriver.implicitly_wait(30)
            self.webdriver.set_page_load_timeout(220)
            logger.info('Unemployment_Crawler-configurações do WEBDRIVER ajustado.')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Falha ao ajustar WEBDRIVER: %s', erro)

    def open_urlsite(self):
        try:
            self.webdriver.get('https://pt.tradingeconomics.com/country-list/employment-rate')
            logger.info('Unemployment_Crawler- URL para uso do CRAWLER aberto.')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Falha ao abrir URL do Crawler: %s', erro)

    def set_tableelement(self):
        try:
            element = self.webdriver.find_element(*PageLocators.TABLE_ELEMENT)
            self.html_content = element.get_attribute('outerHTML')
            logger.info('Unemployment_Crawler-Capturando Elemento da Tabela em HTML.')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Erro ao capiturar elemento da tabela: %s', erro)
    
    def close_webtabs(self):
        try:
            self.webdriver.quit()
            logger.info('Unemployment_Crawler-Aba do navegador fechado com sucesso.')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Erro ao fechar Aba do vavegador: %s', erro)

class Crawler(WebDriver):
    def instace_htmlparser(self):
        try:
            self.soup = BeautifulSoup(self.html_content, 'html.parser')
            logger.info('Unemployment_Crawler-Instanciando  Html.')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Erro ao instanciar o HTML: %s', erro)

    def get_pagetable(self):
        try:
            self.table = self.soup.find(name = 'table')
            logger.info('Unemployment_Crawler-localizando tabela do HTML contente.')
        except Exception as erro:
            logger.error('Unemployment_Crawler-Erro ao localizar tabela do HTML: %s', erro)

class Process(Crawler):
    pass