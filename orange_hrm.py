from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



#Keep Chrome browser open
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()

#Launch application
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

#Allows the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

wait = 2

#To login
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(wait)

driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(wait)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(wait)

# Admin page
driver.find_element(By.XPATH, "//span[text()='Admin']").click()
time.sleep(wait)

# User Management
driver.find_element(By.XPATH, "//span[text()='User Management ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Users']").click()
time.sleep(wait)

# Job
driver.find_element(By.XPATH, "//span[text()='Job ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Job Titles']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Job ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Pay Grades']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Job ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Employment Status']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Job ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Job Categories']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Job ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Work Shifts']").click()
time.sleep(wait)

# Organisation
driver.find_element(By.XPATH, "//span[text()='Organization ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='General Information']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Organization ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Locations']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Organization ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Structure']").click()
time.sleep(wait)

# Qualification
driver.find_element(By.XPATH, "//span[text()='Qualifications ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Skills']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Qualifications ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Education']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Qualifications ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Licenses']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Qualifications ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Languages']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Qualifications ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Memberships']").click()
time.sleep(wait)

#Nationalities
driver.find_element(By.XPATH, "//a[text()='Nationalities']").click()
time.sleep(wait)

# Corporate Branding
driver.find_element(By.XPATH, "//a[text()='Corporate Branding']").click()
time.sleep(wait)

# Configuration
driver.find_element(By.XPATH, "//span[text()='Configuration ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Email Configuration']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Configuration ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Email Subscriptions']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Configuration ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Localization']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Configuration ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Language Packages']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Configuration ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Modules']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Configuration ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Social Media Authentication']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Configuration ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Register OAuth Client']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//span[text()='Configuration ']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='LDAP Configuration']").click()
time.sleep(wait)

# Logout
driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
time.sleep(wait)
driver.find_element(By.XPATH, "//a[text()='Logout']").click()
time.sleep(wait)