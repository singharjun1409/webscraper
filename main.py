from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
# from selenium.common import TimeoutException

# Setup
options = Options()
options.add_argument("--headles=new") # Saving resources by running without UI
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.set_window_size(1920, 1080)
url = "https://finance.yahoo.com/markets/stocks/most-active/"
driver.get(url)

stocks = dict()

# scraping logic...
WebDriverWait(driver, 3)
table = driver.find_element(By.CLASS_NAME , "yf-hhhli1")
'''head = table.find_element(By.TAG_NAME , "thead").find_elements(By.TAG_NAME, "th")
print(headers)'''
body = table.find_element(By.TAG_NAME , "tbody")
rows = body.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME , "td")
    data = {"Name": cols[1].text,"Symbol": cols[0].text , "Price": cols[3].text , "Change": cols[4].text}
    stocks[cols[1].text] = data


# Storing in database
csv_header = ["Name" , "Symbol" , "Price" , "Change"]
with open('stocks.csv', 'w', newline='') as output:
    dict_writer = csv.DictWriter(output, csv_header)
    dict_writer.writeheader()
    dict_writer.writerows(stocks.values())

# close the browser and free up the resources
driver.quit()