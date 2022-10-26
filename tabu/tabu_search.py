from util import consts
import json
from tabu import tabu_list
from tabu import neighbourhood
from operator import attrgetter
from typing import List



class TabuSearch:
    """
    class that runs tabu search algorithm
    """

    def __init__(self) -> None:
        self.num_of_iterations = consts.TABU_ITERATIONS
        self.tabu_list = tabu_list.TabuList()

    def _read_cities(self) -> List[list]:
        """
        method that read cities from a json file and sets it as the start solution
        """
        start_solution = []
        with open(consts.PATH_TO_CITIES, 'r') as file:
            data = json.load(file)

            for name, location in data.items():
                start_solution.append([name, location[0], location[1]])

        return start_solution

    def search(self) -> None:
        """
        method that searches for optimal solution
        it follows the tabu search algorithm
        """
        self.best_solution = neighbourhood.Neighbourhood(self._read_cities())
        self.tabu_list.insert_hood(self.best_solution)
        print("Initial city route: {}".format(self.best_solution.return_city_order()))
        print("Initial route cost: {}".format(self.best_solution.cost))
        for _ in range(consts.TABU_ITERATIONS):
            self.tabu_list.reduce_limit()
            possible_candidates = []

            for candidate in self.best_solution.return_candidates():
                if not self.tabu_list.check_if_tabu(candidate):
                    candidate.calculate_cost()
                    possible_candidates.append(candidate)

            self.best_solution = min(possible_candidates, key=attrgetter('cost'))
            self.tabu_list.insert_hood(self.best_solution)

        print("Result city route: {}".format(self.best_solution.return_city_order()))
        print("Result route cost: {}".format(self.best_solution.cost))
        # for city in self.best_solution.hood:
        #     print(str(city[1])+','+str(city[2]))
