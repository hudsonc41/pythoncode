import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# setup chrome webdriver
driver = webdriver.Chrome()

# load the web page
driver.get("https://wikipedia.com")

# print page source
print(driver.page_source)

# close the driver
driver.quit()
