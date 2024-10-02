from getdata import json_from_request
from datetime import datetime

base = 'https://swapi.dev/api/'

def get_all_planets():
    endpoint = 'planets/'
    info = json_from_request(base, endpoint)
    return info

def get_all_info(category):
    endpoint = f'{category}/'
    info = json_from_request(base, endpoint)
    return info

def in_catergory(item_name):
    return item_name.get('name') == item_name

def provide_population(item_name):
    return item_name.get('population')

if __name__ == 'main':
    startTime = datetime.now()
    planets = get_all_planets()
    print(f"Finished getting data in {datetime.now() - startTime}.")
    condition = input('What do climate do you prefer? ')
    while condition:
        if condition == 'quit':
            break
        print('Here is a list of all planets that match your condition: ')
        planets.sort(key=lambda planet: planet.get('name'))
        planets_match = []
        for planet in planets:
            if planet.get('climate').lower() == condition.lower():
                planets_match.append(planet)   
        if planets_match:
            for planet in planets_match:
                print(f'> {planet.get('name')}')  
                print(f'  * Population: {planet.get('population')}')
                print(f'  * Biomes: {planet.get('terrain')}')
        else:
            print('No planets match your condition.')
        condition = input('What do climate do you prefer? ')

    print(f'Finished. Runtime: {datetime.now() - startTime}.')



