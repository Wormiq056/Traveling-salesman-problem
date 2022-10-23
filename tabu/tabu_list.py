from util import consts
from tabu import neighbourhood


class TabuList:
    """
    class that stores tabu history
    """

    def __init__(self) -> None:
        self.tabu_history = [None for _ in range(consts.TABU_SIZE)]
        self.tabu_history_dict = {}

    def insert_hood(self, hood: neighbourhood) -> None:
        """
        method that inserts neighbourhood into tabu history
        :param hood: hood you want to insert
        """
        city_order = hood.return_city_order()
        self.tabu_history.insert(0, city_order)
        self.tabu_history_dict[tuple(city_order)] = consts.TABU_LIMIT
        last_city = self.tabu_history[-1]
        if last_city is not None:
            del self.tabu_history_dict[tuple(last_city)]
        self.tabu_history.pop()

    def reduce_limit(self) -> None:
        """
        method that reduces tabu limit in hoods that are currently in tabu history
        """
        for hood in self.tabu_history:
            if hood is not None:
                self.tabu_history_dict[tuple(hood)] -= 1
                if self.tabu_history_dict[tuple(hood)] == 0:
                    del self.tabu_history_dict[tuple(hood)]
                    self.tabu_history.remove(hood)

    def check_if_tabu(self, hood: neighbourhood.Neighbourhood) -> bool:
        """
        method that checks if given neighbourhood is currently in tabu history
        :param hood: neighbourhood you want to check
        :return: True or False based on check result
        """
        if self.tabu_history_dict.get(tuple(hood.return_city_order())) is None:
            return False
        return True
