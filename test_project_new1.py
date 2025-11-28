import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.options import Options

from selenium.webdriver.support.ui import Select




def test_validlogin():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://selenium-grid:4444/wd/hub",
        options=options
    )

    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("student")
    driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("Password123")
    driver.find_element(By.XPATH,'//button[@id="submit"]').click()

    if driver.find_element(By.XPATH,"//h1[contains(text(),'Logged In Successfully')]").text=='Logged In Successfully':
        driver.save_screenshot("C:\\Magento_Automation\\selenium_practice\\screenshot28.10.25.png")
        print("Login successful")
    else:
        print("Login failed")

    driver.quit()
