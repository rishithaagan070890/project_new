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
    driver = webdriver.Chrome()
    driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
    driver.maximize_window()
    driver.find_element(By.XPATH,'//span[contains(text(),"Demo Webtable 1 (Static Table)")]')

    def get_celldata(row,column):
        cell_data=driver.find_elements(By.XPATH,f'(//table[@id="customers"]/descendant::tr[{row}]/descendant::span[{column}])')
        for items in cell_data:
            print(items.text, end="  ")

    for row in range(1,8):
       for column in range(1,4):
           if column==2:
               continue
           else:
               get_celldata(row,column)
       print()


def test_getstructureheight():
    driver = webdriver.Chrome()
    driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
    driver.maximize_window()
    driver.find_element(By.CLASS_NAME,"tsc_table_s13")
    i=0
    for j in range(1, 5):
        height = driver.find_element(By.XPATH, f'//table[@class="tsc_table_s13"]/descendant::tr/descendant::td[4*{j}+{i}]')

        print(i,(height.text))
        i+=2
