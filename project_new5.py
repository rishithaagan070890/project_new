import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

#
# Open the webpage:
# 🔗 https://www.techlistic.com/p/demo-selenium-practice.html
#
# Scroll down to the “Automation Practice Table” section.
#
# Perform the following using Selenium:
#
# ✅ Extract all the rows and columns from the table.
#
# ✅ Print the company name and its country for each row.
#
# ✅ Find the row where the structure height is the maximum and print that row’s full details.
#
# ✅ Take a screenshot of the table area and save it (e.g., table_data.png).


def test_extracttabledata():
    driver=webdriver.Chrome()
    driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
    driver.maximize_window()
    driver.find_element(By.XPATH,'//span[contains(text(),"Demo Webtable 1 (Static Table)")]')
    table_row=driver.find_elements(By.XPATH,'//table[@id="customers"]/descendant::tr')
    table_data = driver.find_elements(By.XPATH, '//table[@id="customers"]/descendant::tr/descendant::th')
    for row in range(0,7):
        for table_data=driver.find_elements(By.XPATH,'//table[@id="customers"]/descendant::tr[i]/descendant::th')
        for table_data in table_data:
            print(table_data.text)
