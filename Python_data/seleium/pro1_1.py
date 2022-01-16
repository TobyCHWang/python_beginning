from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH= Service("C:/Users/Toby/PycharmProjects/pythonProject/project1/chromedriver.exe")

driver=webdriver.Chrome(service=PATH)

driver.get("https://google.com")
search= driver.find_element(By.NAME,"q")
search.send_keys("比特幣")

# keys
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()