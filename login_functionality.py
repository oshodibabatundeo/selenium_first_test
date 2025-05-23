from selenium import webdriver
from selenium.webdriver.common.by import By  #To locate elements by css selector, ID or XPATH
from selenium.webdriver.chrome.options import Options  #To keep the browser open after script ends
# from selenium.webdriver.support.ui import WebDriverWait #Lets the script waits as long as needed when loading

import time

wait = 3

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()


time.sleep(wait)

driver.find_element(By.XPATH, '//*[@id="email-id"]').send_keys("confixhub@test.com")
time.sleep(wait)

driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Test001")
time.sleep(wait)

driver.find_element(By.XPATH, '//*[@id="remember"]').click()
time.sleep(wait)

driver.find_element(By.XPATH, '//*[@id="submit-id"]').click()
time.sleep(wait)

driver.find_element(By. XPATH, '/html/body/nav/a').click()
time.sleep(wait)




