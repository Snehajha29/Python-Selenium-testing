from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
def test_options():

    driver=webdriver.Chrome()
    driver.get("http://saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.get_screenshot_as_file("ss.png")
    static_d= driver.find_element(By.CLASS_NAME, "product_sort_container")
    select= Select(static_d)

    # select.select_by_index(2)
    # time.sleep(3)
    set=select.select_by_visible_text("Name (Z to A)")
    # time.sleep(3)
    # select.select_by_value("hilo")
    
    time.sleep(3)