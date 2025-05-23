import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wait = 2

driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()

time.sleep(wait)

email_address = driver.find_element(By.CSS_SELECTOR, '#email-id')
email_address.send_keys("confix@gmail.com")
time.sleep(wait)

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("Amen111")
time.sleep(wait)

click_remember_me_button = driver.find_element(By.CSS_SELECTOR, '#remember')
click_remember_me_button.click()
time.sleep(wait)

click_submit = driver.find_element(By.CSS_SELECTOR, '#submit-id')
click_submit.click()
time.sleep(wait)