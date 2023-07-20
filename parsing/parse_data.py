import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Browser:
    browser, service = None, None

    def __init__(self, login_by: str, login_value: str, pass_by: str, pass_value: str, button_by: str, button_value: str, data_by: str, data_value: str, url: str, username: str, password: str, pos_arg: int = 0):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.service = Service()
        self.browser = webdriver.Chrome(
            service=self.service, options=chrome_options)
        self.login_by = login_by
        self.login_value = login_value
        self.pass_by = pass_by
        self.pass_value = pass_value
        self.button_by = button_by
        self.button_value = button_value
        self.data_by = data_by
        self.data_value = data_value
        self.url = url
        self.username = username
        self.password = password
        self.pos_arg = pos_arg

    def open_page(self):
        self.browser.get(self.url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login(self):
        try:
            elem = WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((self.button_by, self.button_value)))
        finally:
            self.add_input(by=self.login_by,
                           value=self.login_value, text=self.username)
            self.add_input(by=self.pass_by,
                           value=self.pass_value, text=self.password)
            self.click_button(by=self.button_by, value=self.button_value)

    def get_data(self):
        try:
            elem = WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((self.data_by, self.data_value)))
        finally:
            data_element = self.browser.find_element(
                by=self.data_by, value=self.data_value)
            return float(data_element.text.split()[
                self.pos_arg].replace(',', '.'))


if __name__ == '__main__':
    pass
