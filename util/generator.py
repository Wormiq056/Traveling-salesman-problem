import consts
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
        cities[str(i)] = [x, y]

    with open('../data/cities.json', 'w') as file:
        json.dump(cities, file)

generate_cities()
