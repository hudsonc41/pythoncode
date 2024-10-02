import tourism
import getdata
import requests
from datetime import datetime


class API_Data:

    def __init__(self, data, data_type):
        self.data = data
        self.data_type = data_type

    def type(self):
        return self.data_type

    def __str__(self):
        return self

    def sort(self):
        self = sorted(self)

    def get(self, item):
        if self.get(item):
            return self.get(item)
        else:
            return None


planet_data = API_Data(get_all_planets(), "planets")
print(planet_data.get("population"))
print(planet_data)
