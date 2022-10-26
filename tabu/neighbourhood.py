import math
from typing import List


class Neighbourhood:
    """
    class that handles neighbourhood functionalities
    """

    def __init__(self, list_of_cities, calc_cost=True, last_neighbour=(0, 0)):
        self.hood = list_of_cities
        if calc_cost:
            self.cost = self._calculate_cost()
        else:
            self.cost = 0
        self.last_neighbour = tuple(last_neighbour)

    def _calculate_cost(self) -> float:
        """
        mathod that is called when class object is created and you wanto to calculate its path cost
        :return: distance of city order path
        """
        distance = 0.0
        for i in range(len(self.hood)):
            if i == len(self.hood) - 1:
                distance += self._calc_distance(self.hood[i], self.hood[0])
            else:
                distance += self._calc_distance(self.hood[i], self.hood[i + 1])
        return distance

    def calculate_cost(self) -> None:
        """
        method that is called when you want to calculate neighbourhood cost after object was created
        """
        distance = 0.0
        for i in range(len(self.hood)):
            if i == len(self.hood) - 1:
                distance += self._calc_distance(self.hood[i], self.hood[0])
            else:
                distance += self._calc_distance(self.hood[i], self.hood[i + 1])
        self.cost = distance

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

    def return_city_order(self) -> List[str]:
        """
        method that return list of solution path in neighbourhood
        :return: list of cities
        """
        order = []
        for hood in self.hood:
            order.append(hood[0])
        return order

    def return_candidates(self):
        """
        method that yields possible candidates for given neighbourhood
        candidate is created by swaping by rotating order between 2 edges
        :return: possible next neighbourhood
        """
        for i in range(len(self.hood)):
            for j in range(len(self.hood)):
                if i == j:
                    continue
                new_hood = self.hood.copy()
                new_hood[i:j] = reversed(new_hood[i:j])
                yield Neighbourhood(new_hood, calc_cost=False, last_neighbour=(i, j))
