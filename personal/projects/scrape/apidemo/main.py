import requests
from pprint import pprint

base = 'https://swapi.dev/api/'

def json_from_request(base, endpoint, path='', query=''): #='' is a string
    request = f'{base}{endpoint}{path}{query}'
    #print(request)
    response = requests.get(request)
    data = response.json().get('results')
    #pprint(data)
    return data

def get_all_starships():
    endpoint = 'starships/'
    ship_info = json_from_request(base, endpoint)
    print('All starships with hypderdrive raring above 3 are: ')
    for ship in ship_info:
        hyperdrive_rating = float(ship.get('hyperdrive_rating'))
        if hyperdrive_rating > 3:
            print(ship.get('name'))

def get_all_people():
    endpoint = 'people/'
    people_info = json_from_request(base, endpoint)
    return people_info

def in_people(person):
    # if person.get('name') == name:
    #     return True
    # else:
    #     return False

    return person.get('name') == name



get_all_starships()
people_info = get_all_people()
name = input('What character do  you want do know about? ')

found_person = list(filter(in_people, people_info))
if found_person:
    pprint(found_person)
else:
    print('I don\'t know who that is.')











