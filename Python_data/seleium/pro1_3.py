# 常用
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


PATH= Service("C:/Users/Toby/PycharmProjects/pythonProject/project1/chromedriver.exe")

driver=webdriver.Chrome(service=PATH)

driver.get("https://www.dcard.tw/f")
search= driver.find_element(By.NAME,"query")
# clear
search.clear()
search.send_keys("比特幣")

search.send_keys(Keys.RETURN)

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"sc-3yr054-1"))
)

titles=driver.find_elements(By.CLASS_NAME,"tgn9uw-3")

for title in titles:
    print(title.text)

# click
link=driver.find_element(By.LINK_TEXT,"大盤BTC行情很磨嘰，何時才會變盤？")
link.click()
# return previous page
driver.back()
# return
driver.back()
# next
driver.forward()

time.sleep(5)

driver.quit()