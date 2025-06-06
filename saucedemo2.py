from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

wait = 3

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def login():
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(wait)

def add_items_to_cart():
    item_links = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')

    for i in range(len(item_links)):
        item_links = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
        item_links[i].click()
        time.sleep(wait)

        # Add item to cart
        driver.find_element(By.CSS_SELECTOR, 'button.btn_primary').click()
        time.sleep(wait)

        # Go back to the item list
        driver.find_element(By.ID, 'back-to-products').click()
        time.sleep(wait)

def logout():
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link').click()
    # time.sleep(wait)
    
if __name__ == "__main__":
    login()
    add_items_to_cart()
    logout()




