import random
import time
import individual
import fitness
import selection
import mutation

run_time = 1000

random.seed(time)


def solution_found(fed_population):
    for ind in fed_population:
        if ind.fitness == 25:
            print("Solution found")
            return True
    return False


def get_highest_fitness(fed_population):
    highest = individual.Individual()

    for ind in fed_population:
        if ind.fitness > highest.fitness:
            highest = ind
    return highest.fitness


run_count = 0
overall_highest = 0
population = individual.create_individuals()
fitness.evaluate_fitness(population)
print("Original total fitness is: ", fitness.get_total_fitness(population))
print("Original highest fitness is: ", get_highest_fitness(population))

while (run_count < run_time) and not (solution_found(population)):
    print("----------", run_count + 1, "----------")

    if run_count % 100 == 0:
        mutation.mutation_rate -= 0.0001

    population = selection.selection(population)

    fitness.evaluate_fitness(population)

    population = mutation.crossover(population)

    fitness.evaluate_fitness(population)

    population = mutation.mutation(population)

    fitness.evaluate_fitness(population)

    print("Total fitness is: ", fitness.get_total_fitness(population))
    print("Mean fitness is: ", fitness.get_mean_fitness(population, individual.population_number))
    print("Highest fitness is: ", get_highest_fitness(population))
    if get_highest_fitness(population) > overall_highest:
        overall_highest = get_highest_fitness(population)
    print("Overall Highest is: ", overall_highest)

    run_count += 1
