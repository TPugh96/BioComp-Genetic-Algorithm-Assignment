import random
import time
import rule

random.seed(time)
population_number = 100
number_of_genes = 80


class Individual:
    genes = []
    fitness = 0

    def __init__(self):
        self.genes = []
        self.fitness = 0


def create_individuals():
    population = []

    for new_pop in range(0, population_number):
        population.append(Individual())
        for new_gene in range(0, number_of_genes):
            if (new_gene + 1) % (rule.Rule.numberOfConditions + 1) == 0:
                population[new_pop].genes.append(random.randint(0, 1))
            else:
                population[new_pop].genes.append(random.randint(0, 2))

    return population
