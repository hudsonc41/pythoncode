from datetime import datetime
from getdatas import json_from_request
import requests
from bs4 import BeautifulSoup

base = "https://www.sydneyoperahouse.com"
endpoint = "/whats-on"
query = "?page="
path = 0

url = base + endpoint + query + str(path)

print(url)

search = ""

request = requests.get(url)

soup = BeautifulSoup(request.content, "html.parser")

s = soup.find_all("div", class_="card__content")

info = soup.find("div", class_="view-whats-on__settings-info")
no_pages = info.text.split()[8]


for div in s:
    category = div.find("p")
    print(category.text)
    pass
