from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
element = driver.find_element(By.XPATH, "//input[@name='q']")
element.send_keys("Python")
element.send_keys(Keys.RETURN)
driver.implicitly_wait(1000)
