
from util import generator
from genetic import genetic_search as genetic
from util import consts
import time
from tabu import tabu_search as tabu

def test_genetic():
    consts.PATH_TO_CITIES = '../data/cities.json'

    generator.generate_cities_test(20)
    print("******Test - genetic algorithm 20 cities********\n")
    consts.GENETIC_ITERATIONS = 50
    print('TESTING FOR 50 GENETIC ITERATIONS\n')

    print("---TOURNAMENT SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.TOURNAMENTS_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end-start))

    print("---ROULETTTE SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.ROULETTE_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    consts.GENETIC_ITERATIONS = 100
    print('\nTESTING FOR 100 GENETIC ITERATIONS\n')
    print("---TOURNAMENT SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.TOURNAMENTS_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---ROULETTTE SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.ROULETTE_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    consts.GENETIC_ITERATIONS = 200
    print('\nTESTING FOR 200 GENETIC ITERATIONS\n')
    print("---TOURNAMENT SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.TOURNAMENTS_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---ROULETTTE SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.ROULETTE_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    generator.generate_cities_test(30)
    print("\n******Test - genetic algorithm 30 cities********\n")
    consts.GENETIC_ITERATIONS = 50
    print('TESTING FOR 50 GENETIC ITERATIONS\n')

    print("---TOURNAMENT SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.TOURNAMENTS_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---ROULETTTE SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.ROULETTE_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    consts.GENETIC_ITERATIONS = 100
    print('\nTESTING FOR 100 GENETIC ITERATIONS\n')
    print("---TOURNAMENT SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.TOURNAMENTS_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---ROULETTTE SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.ROULETTE_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    consts.GENETIC_ITERATIONS = 200
    print('\nTESTING FOR 200 GENETIC ITERATIONS\n')
    print("---TOURNAMENT SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.TOURNAMENTS_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---ROULETTTE SELECTION---")
    start = time.time()
    genetic.GeneticSearch(consts.ROULETTE_SELECTION)
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

def test_tabu():
    consts.PATH_TO_CITIES = '../data/cities.json'
    generator.generate_cities_test(20)
    print("******Test - tabu search 20 cities********\n")
    consts.TABU_ITERATIONS = 50

    print("\nTESTING TABU SEARCH WITH 50 ITERATIONS\n")
    consts.TABU_SIZE = 10

    print("---TABU LIST SIZE 10---")
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---TABU LIST SIZE 20---")
    consts.TABU_SIZE = 20
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    consts.TABU_ITERATIONS = 100

    print("\nTESTING TABU SEARCH WITH 100 ITERATIONS\n")
    consts.TABU_SIZE = 10

    print("---TABU LIST SIZE 10---")
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---TABU LIST SIZE 20---")
    consts.TABU_SIZE = 20
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    consts.TABU_ITERATIONS = 200

    print("\nTESTING TABU SEARCH WITH 200 ITERATIONS\n")
    consts.TABU_SIZE = 10

    print("---TABU LIST SIZE 10---")
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---TABU LIST SIZE 20---")
    consts.TABU_SIZE = 20
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    generator.generate_cities_test(30)
    print("******Test - tabu search 30 cities********\n")
    consts.TABU_ITERATIONS = 50

    print("\nTESTING TABU SEARCH WITH 50 ITERATIONS\n")
    consts.TABU_SIZE = 15

    print("---TABU LIST SIZE 15--")
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---TABU LIST SIZE 30---")
    consts.TABU_SIZE = 30
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    consts.TABU_ITERATIONS = 100

    print("\nTESTING TABU SEARCH WITH 100 ITERATIONS\n")
    consts.TABU_SIZE = 15

    print("---TABU LIST SIZE 15---")
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---TABU LIST SIZE 30---")
    consts.TABU_SIZE = 30
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    consts.TABU_ITERATIONS = 200

    print("\nTESTING TABU SEARCH WITH 200 ITERATIONS\n")
    consts.TABU_SIZE = 15

    print("---TABU LIST SIZE 15---")
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))

    print("---TABU LIST SIZE 30---")
    consts.TABU_SIZE = 30
    start = time.time()
    tabu.TabuSearch().search()
    end = time.time()
    print("Time to execute algorithm: {} seconds".format(end - start))


def start_testing():
    test_genetic()
    print('\n\n')
    test_tabu()

