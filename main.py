from tabu import tabu_search as tabu
import argparse
from util import generator
from genetic import genetic_search as genetic
from util import consts

def main() -> None:
    """
    main function that based on arguments chooses which search algorithm to run and if new random cities should be generated
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-s",
        type=str,
        help="Specifies algorithm to be used(t = tabu search, g = genetic algorithm). Basic method is tabu search",
    )

    parser.add_argument(
        "-c",
        type=str,
        help="Argument that if set to true (Y) will generate new random cities"
    )
    args = parser.parse_args()
    if args.c is not None:
        if args.c.lower() == 'y':
            generator.generate_cities()
        else:
            if args.c.lower() not in ['y', 'n']:
                print("Parameter -c must be either y or n")
                return

    if args.s is not None:
        if args.s.lower() == 't':
            tabu.TabuSearch().search()
        elif args.s.lower() == 'g':
            genetic.GeneticSearch(consts.TOURNAMENTS_SELECTION)
        else:
            print("Incorrect -p argument. Set it to \'p\' or \'g\' ")
            return
    else:
        genetic.GeneticSearch(consts.ROULETTE_SELECTION)
        #tabu.TabuSearch().search()




if __name__ == "__main__":
    main()
