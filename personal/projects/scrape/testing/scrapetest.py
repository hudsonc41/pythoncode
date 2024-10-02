from datetime import datetime
from testing.getdatas import json_from_request
import requests
from bs4 import BeautifulSoup

url = "https://www.sydneyoperahouse.com"
endpoint = "/whats-on"
query = "?page="
path = 0


request = requests.get(url)

print(request.content)

soup = BeautifulSoup(request.content, "html.parser")

s = soup.find("div", class_="dialog-off-canvas-main-canvas")

lines = s.find("p")

print(s)
print(lines)
