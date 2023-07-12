from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("http://saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print(driver.title)
act_title=driver.title
exp_title="Swag Labs"
if act_title==exp_title:
    print("Login test passed")

else:
    print("Login test failed")

driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack").click()

time.sleep(5)
driver.close()