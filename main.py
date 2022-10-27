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
        help="Specifies algorithm to be used(t = tabu search, g1 = genetic algorithm with tournament selection, "
             "g2 = genetic algorithm with roulette selection). Basic method is tabu search",
    )

    parser.add_argument(
        "-c",
        type=str,
        help="Argument that if set to true (Y) will generate new random cities, if set to T it will rewrite data "
             "for test route"
    )

    args = parser.parse_args()
    
    if args.c is not None:
        if args.c.lower() == 'y':
            generator.generate_cities()
        elif args.c.lower() == 't':
            generator.generate_test()
        else:
            if args.c.lower() not in ['y', 'n']:
                print("Parameter -c must be either y or n or t")
                return

    if args.s is not None:
        if args.s.lower() == 't':
            tabu.TabuSearch().search()
        elif args.s.lower() == 'g1':
            genetic.GeneticSearch(consts.TOURNAMENTS_SELECTION)
        elif args.s.lower() == 'g2':
            genetic.GeneticSearch(consts.ROULETTE_SELECTION)
        else:
            print("Incorrect -p argument. Set it to \'p\' or \'g1\' or \'g2\'")
            return
    else:
        tabu.TabuSearch().search()


if __name__ == "__main__":
    main()
