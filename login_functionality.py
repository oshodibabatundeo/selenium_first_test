from selenium import webdriver
from selenium.webdriver.common.by import By  #To locate elements by css selector, ID or XPATH
from selenium.webdriver.chrome.options import Options  #To keep the browser open after script ends
# from selenium.webdriver.support.ui import WebDriverWait #Lets the script waits as long as needed when loading
from selenium.webdriver.support.ui import Select

import time

wait = 1

# Keep Chrome open after script ends
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Initialize driver 

driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()


time.sleep(wait)

def login():
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

def new_customer():
    driver.find_element(By.XPATH, '//*[@id="email-id"]').send_keys("confixhub@test.com")
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Test001")
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="remember"]').click()
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="submit-id"]').click()
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="new-customer"]').click()
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="EmailAddress"]').send_keys("babatunde@confix.org")
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys("Babatunde")
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys("Oshodi")
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="City"]').send_keys("London")
    time.sleep(wait)

    dropdown = Select(driver.find_element(By.XPATH, '//*[@id="StateOrRegion"]'))
    dropdown.select_by_visible_text("Texas")
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/div[6]/input[1]').click()
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/div[7]/input').click()
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/button').click()
    time.sleep(wait)

def sign_out():
    driver.find_element(By.XPATH, '//*[@id="email-id"]').send_keys("confixhub@test.com")
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Test001")
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="remember"]').click()
    time.sleep(wait)

    driver.find_element(By.XPATH, '//*[@id="submit-id"]').click()
    time.sleep(wait)

    driver.find_element(By.XPATH, '/html/body/nav/ul/li/a').click()
    time.sleep(wait)


# if __name__ == "__main__":

    # To call login function
# login()

# To call new customer function
new_customer()

#To call sign out function
# sign_out()



