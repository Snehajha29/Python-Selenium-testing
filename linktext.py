from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.get("http://saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack").click()
# time.sleep(3)
driver.back()
# time.sleep(3)
# driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
ids = [
    'add-to-cart-sauce-labs-backpack',
    'add-to-cart-sauce-labs-bike-light',
    'add-to-cart-sauce-labs-bolt-t-shirt',

]
for id in ids:
    #driver.find_element(By.XPATH,f"//*[@id='{id}']").click()
    driver.find_element(By.ID, id).click()
    # driver.back()
# driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(3)
driver.find_element(By.ID,"remove-sauce-labs-backpack").click()
driver.find_element(By.ID,"checkout").click()
time.sleep(5)
driver.back()
driver.find_element(By.ID,"continue-shopping").click()
time.sleep(5)
driver.close() 

