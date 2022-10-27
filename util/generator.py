from util import consts
import random
import json


def generate_cities() -> None:
    """
    function that generates random cities
    """
    cities = {}
    for i in range(consts.NUM_OF_CITIES):
        x = random.randint(0, consts.MAP_X)
        y = random.randint(0, consts.MAP_Y)
        cities[str(i + 1)] = [x, y]
        # print(str(x)+','+str(y))
    with open('./data/cities.json', 'w') as file:
        json.dump(cities, file)


def generate_test() -> None:
    """
    method that loads test rout from data/test.txt
    """
    dict = {}
    with open('./data/test.txt', 'r') as file:
        data = json.load(file)

        for city in data.get("config"):
            dict[city.get('Name')] = [city.get('X'), city.get('Y')]
            # print(str(city.get('X'))+",",str(city.get('Y')))
    with open('./data/cities.json', 'w') as file:
        json.dump(dict, file)
