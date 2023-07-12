from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)