from selenium import webdriver
import time
url = "https://www.ok.koec.com.ua/"
driver = webdriver.Chrome(
    executable_path='/Users/galina/Desktop/ProgektBot/chromedriver/chromedriver')

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
