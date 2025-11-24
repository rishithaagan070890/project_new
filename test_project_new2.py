
#
# Use Selenium to:
#
# Open the same login page.
#
# Try invalid credentials.
#
# Verify that the error message appears:
#
# “Your username is invalid!”
#
# Take a screenshot called failed_login.png.
#
# Print a clear message in the console:
#
# “❌ Login failed as expected” if the error appears
#
# # “⚠️ Test failed: error message not shown” if it doesn’t
import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
def test_invalidlogin():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://selenium-hub:4444/wd/hub",
        options=options
    )
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("stuent")
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Password123")
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
    time.sleep(5)
    if driver.find_element(By.XPATH,'//div[@class="show"]').text=="Your username is invalid!":
        driver.save_screenshot("C:\\Magento_Automation\\selenium_practice\\invaliduser_screenshot.png")
        print("Invalid login")
