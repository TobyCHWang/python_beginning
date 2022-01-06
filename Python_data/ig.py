from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

PATH= Service("C:/Users/Toby/PycharmProjects/pythonProject/project1/chromedriver.exe")

driver=webdriver.Chrome(service=PATH)

driver.get("https://www.instagram.com/")

username=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.NAME,"username"))
)

password=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.NAME,"password"))
)

username.clear()
password.clear()

login= driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')

username.send_keys("webhot01")
password.send_keys("2126jstoby30502011")

login.click()

# 頁面跳轉 explicit wait


search=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)

search.clear()

keyword="#dog"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
# ig need two enter

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
)

# scroll
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)


imgs =driver.find_elements(By.CLASS_NAME,"FFVAD")
path=os.path.join(keyword)
os.mkdir(path)

count=0

for img in imgs:
    save_as=os.path.join(path, keyword+str(count)+'.jpg')
    wget.download(img.get_attribute("src"),save_as)
    count+=1






