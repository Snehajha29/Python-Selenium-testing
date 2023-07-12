from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME, "proceed").click()
alt=driver.switch_to.alert
alt.accept()
driver.find_element(By.NAME, "login").send_keys("Selenium")
driver.find_element(By.NAME, "passwd").send_keys("Password")
time.sleep(5)