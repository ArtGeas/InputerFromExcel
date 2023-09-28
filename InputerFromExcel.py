# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# import time

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# try:
#     driver.maximize_window()
#     driver.get("https://rpachallenge.com/")
#     time.sleep(5)
# except Exception as e:
#     print(e)
# finally: 
#     driver.close()
#     driver.quit()




from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.maximize_window()
    driver.get("https://rpachallenge.com/")
    time.sleep(5)
except Exception as e:
    print(e)
finally: 
    driver.close()
    driver.quit()


