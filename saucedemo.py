from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

wait = 4

# Set Chrome options
options = Options()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)

# Launch browser
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(wait)


def login():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(wait)


def add_all_items_to_cart():
    add_buttons = driver.find_elements(By.XPATH, '//button[text()="Add to cart"]')

    for button in add_buttons:
        button.click()
        time.sleep(1)

def logout():
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link').click()
    # time.sleep(wait)

if __name__ == "__main__":
    login()
    add_all_items_to_cart()
    logout()