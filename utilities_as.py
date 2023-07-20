from parsing.parse_data import Browser
from selenium.webdriver.common.by import By
from passw import *
from parsing.parse_data_tg_as import TgParse


class Utilities():

    def internet(self):
        internet_params = {
            'login_by': By.CSS_SELECTOR,
            'login_value': '#maindiv > div > table > tbody > tr > td:nth-child(3) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]',
            'pass_by': By.CSS_SELECTOR,
            'pass_value': '#maindiv > div > table > tbody > tr > td:nth-child(3) > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input[type=password]',
            'button_by': By.XPATH,
            'button_value': '//*[@id="maindiv"]/div/table/tbody/tr/td[3]/form/table/tbody/tr[2]/td[3]/input',
            'data_by': By.XPATH,
            'data_value': '//*[@id="maindiv"]/table/tbody/tr/td[2]/table[3]/tbody/tr[3]/td[2]/span',
            'url': "https://my.simnet.kiev.ua/cgi-bin/stat.pl",
            'username': INTERNET_LOG,
            'password': INTERNET_PASS,
        }
        internet = Browser(**internet_params)
        internet.open_page()
        internet.login()
        i = internet.get_data()
        internet.close_browser()
        return i

    def light(self):
        light_params = {
            'login_by': By.ID,
            'login_value': 'loginform-username',
            'pass_by': By.ID,
            'pass_value': 'loginform-password',
            'button_by': By.NAME,
            'button_value': 'login-button',
            'data_by': By.XPATH,
            'data_value': "(//div[@class='panel-body'])[3]",
            'url': "https://www.ok.koec.com.ua/",
            'username': LIGHT_LOG,
            'password': LIGHT_PASS,
        }
        light = Browser(**light_params)
        light.open_page()
        light.login()
        l = light.get_data()
        light.close_browser()
        return l

    def water(self):
        water_params = {
            'login_by': By.ID,
            'login_value': 'username',
            'pass_by': By.ID,
            'pass_value': 'password',
            'button_by': By.CSS_SELECTOR,
            'button_value': '#main > div > div > div:nth-child(2) > div > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input',
            'data_by': By.CLASS_NAME,
            'data_value': "summary-val-major",
            'url': "http://ok.pbvoda.com.ua",
            'username': WATER_LOG,
            'password': WATER_PASS,
        }
        water = Browser(**water_params)
        water.open_page()
        water.login()
        w = water.get_data()
        water.close_browser()
        return (w)

    async def gas(self):
        gas = TgParse(API_ID, API_HASH, 'GASUA_bot')
        g = await gas.get_gas_tg()
        return (g)

    async def jek(self):
        jek = TgParse(API_ID, API_HASH, 'Wetoo_bot')
        j = await jek.get_jek_tg()
        return (j)

    # def summa(self, list):
    #     summa = 0
    #     for elem in list:
    #         summa = summa + elem
    #     return (round(summa, 2))


# list = Utilities()
# my_list = (list.internet(), list.gas(), list.jek(), list.light(), list.water())
# summa = list.summa(my_list)
