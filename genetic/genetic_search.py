from operator import attrgetter

from util import consts
import random as r
import json
from typing import List
from genetic import chromosome

r.seed(consts.SEED)


class GeneticSearch:
    best_solution: chromosome.Chromosome
    in_order_solution: chromosome.Chromosome

    def __init__(self, parent_selection):
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

    def _generate_population(self):
        self.in_order_solution = chromosome.Chromosome(self._read_cities())
        first_chomosome = self.in_order_solution.genes
        r.shuffle(first_chomosome)
        population = [chromosome.Chromosome(first_chomosome)]
        for i in range(consts.INITIAL_POPULATION - 1):
            new_population = (population[i].genes.copy())
            r.shuffle(new_population)
            population.append(chromosome.Chromosome(new_population))

        return population

    def _roullete_selection(self):
        worst_solution = max(self.population, key=attrgetter('fitness'))
        selected_parents = []
        sum_of_finesses = 0
        for chromosome in self.population:
            fitness_value = worst_solution.fitness - chromosome.fitness
            sum_of_finesses += fitness_value

        if sum_of_finesses == 0:
            return selected_parents

        for i in range(int(consts.INITIAL_POPULATION * (0.64))):
            j = 0
            random_stop_point = r.randint(0, int(sum_of_finesses))
            while random_stop_point >= 0:
                stop_minus = worst_solution.fitness - self.population[j].fitness
                random_stop_point -= stop_minus
                if random_stop_point > 0:
                    j += 1

            selected_parents.append(self.population[j])
            self.selection_winners[tuple(self.population[j].return_city_order())] = True
        return selected_parents

    def _tournament_selection(self):
        selected_parents = []
        while len(selected_parents) != int(consts.INITIAL_POPULATION * (0.64)):
            tournament = r.sample(self.population, int(consts.INITIAL_POPULATION * (0.1)))
            winner = min(tournament, key=attrgetter('fitness'))

            self.selection_winners[tuple(winner.return_city_order())] = True
            selected_parents.append(winner)
        return selected_parents

    def _create_random_chromosomes(self):
        new_randoms = []
        for i in range(int(consts.INITIAL_POPULATION * (0.08))):
            new_chromosome = self.in_order_solution.genes
            r.shuffle(new_chromosome)
            new_randoms.append(chromosome.Chromosome(new_chromosome))
        return new_randoms

    def _mutate_chromosomes(self, chromosomes):
        mutated = []
        for chromie in chromosomes:
            start = r.randint(0, len(chromie.genes) - 1)
            end = r.randint(start + 1, len(chromie.genes))
            new_genes = chromie.genes.copy()
            new_genes[start:end] = reversed(new_genes[start:end])
            mutated.append(chromosome.Chromosome(new_genes))
        return mutated

    def _create_offsprings(self, parents):
        offsprings = []
        for i in range(0, int(len(parents) / 2)):
            start = r.randint(0, len(parents[i].genes) - 1)
            end = r.randint(start + 1, len(parents[i].genes))
            offspring_end = parents[i].genes[start:end]
            parent2_copy = parents[i + 1].genes.copy()
            for city in offspring_end:
                parent2_copy.remove(city)
            offspring = parent2_copy + offspring_end
            offsprings.append(chromosome.Chromosome(offspring))

            start = r.randint(0, len(parents[i].genes) - 1)
            end = r.randint(start + 1, len(parents[i].genes))
            offspring_end = parents[i + 1].genes[start:end]
            parent1_copy = parents[i].genes.copy()
            for city in offspring_end:
                parent1_copy.remove(city)
            offspring = parent1_copy + offspring_end
            offsprings.append(chromosome.Chromosome(offspring))
            i += 1
        return offsprings

    def _run(self):
        for i in range(consts.GENETIC_ITERATIONS):
            finish_counter = 0
            if self.parent_selection == consts.TOURNAMENTS_SELECTION:
                selected_parents = self._tournament_selection()
            elif self.parent_selection == consts.ROULETTE_SELECTION:
                selected_parents = self._roullete_selection()
                if not selected_parents:
                    return True
            else:
                print("No valid parent selection method chosen (1 - tournaments selection, 2 - roulette selection")
                return False
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
            new_chromosomes = self._create_random_chromosomes()
            mutated_chromosomes = self._mutate_chromosomes(mutating_chromosomes)
            offsprings = self._create_offsprings(selected_parents)

            self.population = self.population + new_chromosomes + mutated_chromosomes + offsprings
            self.population.sort(key=lambda x: x.fitness)
            self.population = self.population[:consts.INITIAL_POPULATION]
            self.selection_winners.clear()
