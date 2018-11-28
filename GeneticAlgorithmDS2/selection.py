import individual
import random
import time


random.seed(time)


def selection(population):
    offspring = []
    while len(offspring) < individual.population_number:
        new_offspring = individual.Individual()
        winner = tournament_selection(population)
        for gene in winner.genes:
            new_offspring.genes.append(gene)
        offspring.append(new_offspring)
    return offspring


def tournament_selection(population):
    random_parent_one = random.randint(0, individual.population_number - 1)
    random_parent_two = random.randint(0, individual.population_number - 1)
    while random_parent_one == random_parent_two:
        random_parent_one = random.randint(0, individual.population_number - 1)
        random_parent_two = random.randint(0, individual.population_number - 1)

    parent_one = population[random_parent_one]
    parent_two = population[random_parent_two]

    if parent_one.fitness > parent_two.fitness:
        return parent_one
    else:
        return parent_two
