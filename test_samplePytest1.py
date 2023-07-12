from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time


def test_sample1():
    driver=webdriver.Chrome()
    driver.get("http://saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print(driver.title)
    act_title=driver.title
    exp_title="Swag Labs"
    assert act_title==exp_title

    driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack").click()
    assert '$29.99' in driver.page_source
    # time.sleep(5)
    driver.close()

    