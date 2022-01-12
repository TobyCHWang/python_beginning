#selenium
# action chains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

PATH= Service("C:/Users/Toby/PycharmProjects/pythonProject/project1/chromedriver.exe")

driver=webdriver.Chrome(service=PATH)

driver.get("https://tsj.tw/")

actions =ActionChains(driver)

blow=driver.find_element(By.ID,"click")
# x-path
blow_count=driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')

items=[]
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'))
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]/i'))

prices=[]
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))



for i in range(10000):
    actions.click(blow).perform()
    count=int(blow_count.text.replace("您目前擁有","").replace("技術點",""))

    for j in range(3):
        price=int(prices[j].text.replace("技術點",""))
        if price<=count:
            upgrade_action=ActionChains(driver)
            upgrade_action.move_to_element(items[j])
            upgrade_action.click().perform()

            break


