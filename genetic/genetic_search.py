from operator import attrgetter

from util import consts
import random as r
import json
from typing import List
from genetic.chromosome import Chromosome

# setting seed so random usages can be replicated
r.seed(consts.SEED)


class GeneticSearch:
    """
    class that runs the genetic search algorithm
    """
    best_solution: Chromosome
    in_order_solution: Chromosome

    def __init__(self, parent_selection: int) -> None:
        self.population = self._generate_population()
        self.parent_selection = parent_selection
        self.selection_winners = {}
        self._run()
        self.best_solution = self.population[0]
        print(self.best_solution.fitness)

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

    def _generate_population(self) -> List[Chromosome]:
        """
        this method generates random populations based on number in consts
        :return: returns list of randomly generated chromosome objects
        """
        self.in_order_solution = Chromosome(self._read_cities())
        first_chomosome = self.in_order_solution.genes
        r.shuffle(first_chomosome)
        population = [Chromosome(first_chomosome)]
        for i in range(consts.INITIAL_POPULATION - 1):
            new_population = (population[i].genes.copy())
            r.shuffle(new_population)
            population.append(Chromosome(new_population))

        return population

    def _roullete_selection(self) -> List[Chromosome]:
        """
        this is one of two parents selection method
        this method randomly selects parents from a roulette wheel, the more fitter the parent the bigger chance
        it has to be selected for mating
        this selection is run for until 64% of parents were selected from all population
        :return: selected number of parents that were chosen on spinning wheel
        """
        worst_solution = max(self.population, key=attrgetter('fitness'))
        selected_parents = []
        sum_of_finesses = 0

        # calculating fitness value from worst node so that cost is reversed
        for chromosome in self.population:
            fitness_value = worst_solution.fitness - chromosome.fitness
            sum_of_finesses += fitness_value

        # edge case that happends when curent population is full of duplicate chromosomes
        if sum_of_finesses == 0:
            return selected_parents

        # for loop for spinning the wheel once wheel stops select parent
        for i in range(int(consts.INITIAL_POPULATION * (0.64))):
            j = 0
            random_stop_point = r.randint(0, int(sum_of_finesses))
            while random_stop_point >= 0:
                stop_minus = worst_solution.fitness - self.population[j].fitness
                random_stop_point -= stop_minus
                if random_stop_point > 0:
                    j += 1

            selected_parents.append(self.population[j])
            # remember selected parent
            self.selection_winners[tuple(self.population[j].return_city_order())] = True
        return selected_parents

    def _tournament_selection(self) -> List[Chromosome]:
        """
        method that selects parents for creation of offsprings
        this tournament chooses random 1/10th from population and selects best chromosome based on its cost
        this selection is run for until 64% of parents were selected from all population
        :return: selected parents that won the tournament
        """
        selected_parents = []
        while len(selected_parents) != int(consts.INITIAL_POPULATION * (0.64)):
            tournament = r.sample(self.population, int(consts.INITIAL_POPULATION * (0.1)))
            winner = min(tournament, key=attrgetter('fitness'))

            self.selection_winners[tuple(winner.return_city_order())] = True
            selected_parents.append(winner)
        return selected_parents

    def _create_random_chromosomes(self) -> List[Chromosome]:
        """
        method that creates completely random new chromosomes for 8% of the population mix
        :return: randomly generated chromosomes
        """
        new_randoms = []
        for i in range(int(consts.INITIAL_POPULATION * (0.08))):
            new_chromosome = self.in_order_solution.genes
            r.shuffle(new_chromosome)
            new_randoms.append(Chromosome(new_chromosome))
        return new_randoms

    def _mutate_chromosomes(self, chromosomes: List[Chromosome]) -> List[Chromosome]:
        """
        method that mutates randomly selected 28% chromosomes that were not selected for parenting
        mutation is done just by reversing random indexes in chromosomes genes
        :param chromosomes: randomly selected chromosomes
        :return: randomly mutated given chromosomes
        """
        mutated = []
        for chromie in chromosomes:
            start = r.randint(0, len(chromie.genes) - 1)
            end = r.randint(start + 1, len(chromie.genes))
            new_genes = chromie.genes.copy()
            new_genes[start:end] = reversed(new_genes[start:end])
            mutated.append(Chromosome(new_genes))
        return mutated

    def _create_offsprings(self, parents: List[Chromosome]) -> List[Chromosome]:
        """
        method that creates offspring for selected parents
        offsprings are created based on cross over
        from 1st parent we select random part of genes that we remove from copied 2nd parent, we keep genes that were
        not removed from 2nd parent and fill the rest with shuffled genes that we selected from the 1st parent at start
        we repeat the proccess but which parent 1 for parent 2
        then at the end append created offsprings to return list
        :param parents: selected parents for mating
        :return: created offsprings from parents
        """
        offsprings = []
        for i in range(0, int(len(parents) / 2)):
            # first offspring creation
            start = r.randint(0, len(parents[i].genes) - 1)
            end = r.randint(start + 1, len(parents[i].genes))
            offspring_end = parents[i].genes[start:end]
            parent2_copy = parents[i + 1].genes.copy()
            for city in offspring_end:
                parent2_copy.remove(city)
            offspring = parent2_copy + offspring_end
            offsprings.append(Chromosome(offspring))

            # second offspring creation
            start = r.randint(0, len(parents[i].genes) - 1)
            end = r.randint(start + 1, len(parents[i].genes))
            offspring_end = parents[i + 1].genes[start:end]
            parent1_copy = parents[i].genes.copy()
            for city in offspring_end:
                parent1_copy.remove(city)
            offspring = parent1_copy + offspring_end
            offsprings.append(Chromosome(offspring))
            i += 1
        return offsprings

    def _run(self) -> bool:
        """
        method that runs the genetic algorithm
        it chooses 64% of the population for mating, 28% of the population for random mutating and 8% of the population
        for creation of random new chromosomes
        :return: bool if algorithm ran successfully
        """
        for i in range(consts.GENETIC_ITERATIONS):
            finish_counter = 0
            # choosing which parent selection algorithm to use
            if self.parent_selection == consts.TOURNAMENTS_SELECTION:
                selected_parents = self._tournament_selection()
            elif self.parent_selection == consts.ROULETTE_SELECTION:
                selected_parents = self._roullete_selection()
                # if roulette selection did not return any chromosomes end algorithm
                if not selected_parents:
                    return True
            else:
                print("No valid parent selection method chosen (1 - tournaments selection, 2 - roulette selection")
                return False

            # choosing random chromosomes for mutation that were not selected for mating
            mutating_chromosomes = []
            while len(mutating_chromosomes) != int(consts.INITIAL_POPULATION * (0.28)):
                if finish_counter == consts.GENETIC_ITERATIONS + 100:
                    return True
                random_chromosome = r.choice(self.population)
                if self.selection_winners.get(tuple(random_chromosome.return_city_order())):
                    finish_counter += 1
                    continue
                finish_counter = 0
                mutating_chromosomes.append(random_chromosome)
            # generating random chromosomes
            new_chromosomes = self._create_random_chromosomes()

            # mutating chromosomes that were selected for mutation
            mutated_chromosomes = self._mutate_chromosomes(mutating_chromosomes)

            # creation of offsprings from parents that were selected
            offsprings = self._create_offsprings(selected_parents)

            # add all chromosomes to population
            self.population = self.population + new_chromosomes + mutated_chromosomes + offsprings
            # sort them by fitness
            self.population.sort(key=lambda x: x.fitness)
            # remember only the best half
            self.population = self.population[:consts.INITIAL_POPULATION]

            # clear memory of chromosomes that were selected in this loop
            self.selection_winners.clear()
