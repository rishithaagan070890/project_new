import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import Select

#
# Open the above URL.
#
# Fill in:
#
# First Name: Rishitha
#
# Last Name: Naga
#
# Select Gender: Female
#
# Select Profession: Automation Tester
#
# Choose Continent: Asia (from dropdown)
#
# Take a screenshot after submission.
#
# Print:
#
# ✅ Form selections completed successfully.
# Screenshot saved.


def test_formsubmission2():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
    driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
    driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("Rishitha")
    driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys("Naga")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@name="sex" and @value="Female"]').click()
    driver.find_element(By.XPATH,'//input[@name="profession" and @value="Automation Tester"]').click()
    driver.find_element(By.XPATH,'//select[@id="continents"]')
    select=Select(driver.find_element(By.XPATH,'//select[@id="continents"]')).select_by_visible_text("Asia")
    driver.save_screenshot("C:\\Magento_Automation\\selenium_practice\\formsubmission.png")
    print("✅ Form selections completed successfully.\n Screenshot saved.")