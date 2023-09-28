from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


url = "https://rpachallenge.com/"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
driver.get(url)
time.sleep(5)

driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelFirstName')]").send_keys('kuku')
driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelLastName')]").send_keys('kuku')
driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelCompanyName')]").send_keys('kuku')
driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelRole')]").send_keys('kuku')
driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelAddress')]").send_keys('kuku')
driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelEmail')]").send_keys('kuku')
driver.find_element(By.XPATH, "//*[contains(@ng-reflect-name,'labelPhone')]").send_keys('kuku')

time.sleep(5)


driver.close()
driver.quit()


