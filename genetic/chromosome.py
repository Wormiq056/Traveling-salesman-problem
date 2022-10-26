import math
import random as r
from util import consts

r.seed(consts.SEED)


class Chromosome:
    def __init__(self, city_order):
        self.genes = city_order
        self.fitness = self._calculate_cost()

    def _calculate_cost(self) -> float:
        """
        mathod that is called when class object is created and you wanto to calculate its path cost
        :return: distance of city order path
        """
        distance = 0.0
        for i in range(len(self.genes)):
            if i == len(self.genes) - 1:
                distance += self._calc_distance(self.genes[i], self.genes[0])
            else:
                distance += self._calc_distance(self.genes[i], self.genes[i + 1])
        return distance

    def _calc_distance(self, city_a, city_b) -> float:
        """
        helper method that calculates distance from city_a to city_b using pythagorean theorem
        :param city_a: first city
        :param city_b: second city
        :return: calculated distance between cities
        """
        a = abs(city_a[1] - city_b[1])
        b = abs(city_a[2] - city_b[2])
        return math.sqrt(a ** 2 + b ** 2)

    def return_city_order(self):
        order = []
        for city in self.genes:
            order.append(city[0])
        return order
