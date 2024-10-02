import requests
from pprint import pprint

base = 'https://swapi.dev/api/'

def json_from_request(base, endpoint, path='', query=''):
    request = f'{base}{endpoint}{path}{query}'
    response = requests.get(request)
    data = response.json().get('results')
    return data

def get_all_info(category):
    endpoint = f'{category}/'
    info = json_from_request(base, endpoint)
    return info

def in_catergory(item_name):
    return item_name.get('name') == item_name

interest = input('What would you like to know? ')
while interest:
    try:
        info = get_all_info(interest)
        print(f'Here is a list of all the {interest}: ')
        for info in info:
            print(f'* {info.get('name')}')
    except:
        print('No information found.')
    interest = input('What would you like to know? ')




