from datetime import datetime
from getdatas import json_from_request
import requests
from bs4 import BeautifulSoup

base = "https://www.sydneyoperahouse.com"
endpoint = "/whats-on"
query = "?page="
path = 0

url = url = base + endpoint + query + str(path)

request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")
info = soup.find("div", class_="view-whats-on__settings-info")
no_pages = int(info.text.split()[8]) // 12  # each page has 12 events
"""
search_type = input("musician: m, composer: c, genre: g, date: d, venue: v, quit: q")
while search_type:
    if search_type not in "mcgdv":
        print("Invalid")
    elif search_type == "q":
        exit()
    else:
        break


def search_for():
    search_item = input("Search for:")
    if search_type == "m":
        region = ""
"""

for i in range(no_pages + 1):
    url = url = base + endpoint + query + str(path)
    print(url)
    info = soup.find("div", class_="view-whats-on__settings-info")
    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    s = soup.find_all("div", class_="card__content")
    for div in s:
        category = div.find("p").text
        name = div.find("span").text
        if category == "Classical Music":
            print(name)
    path += 1
