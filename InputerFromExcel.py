from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time


# читаем excel файл
df = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')    

# вставляем данные в форму 
url = "https://rpachallenge.com/"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get(url)

driver.find_element(By.XPATH, "//*[contains(@class,'waves-effect col s12 m12 l12 btn-large uiColorButton')]").click()

for index, row in df.iterrows():

    driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelFirstName')]").send_keys(row['First Name'])
    driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelLastName')]").send_keys(row['Last Name'])
    driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelCompanyName')]").send_keys(row['Company Name'])
    driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelRole')]").send_keys(row['Role in Company'])
    driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelAddress')]").send_keys(row['Address'])
    driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelEmail')]").send_keys(row['Email'])
    driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelPhone')]").send_keys(row['Phone Number'])
    driver.find_element(By.XPATH, "//*[contains(@class,'btn uiColorButton')]").click()

# driver.close()
# driver.quit()


