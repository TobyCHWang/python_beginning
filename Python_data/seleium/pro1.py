#selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PATH= Service("C:/Users/Toby/PycharmProjects/pythonProject/project1/chromedriver.exe")

driver=webdriver.Chrome(service=PATH)

driver.get("https://google.com")

print(driver.title)

driver.quit()