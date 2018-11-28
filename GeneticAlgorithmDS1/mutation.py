import random
import time
import individual
import rule

random.seed(time)
crossover_rate = 0.75
mutation_rate = 0.004


def crossover(population):
    pop_count = 0
    while pop_count < individual.population_number:
        if crossover_rate * 100 > random.randint(0, 100):
            print("crossover")
            crossover_point = random.randint(0, individual.number_of_genes - 1)
            l1 = population[pop_count].genes[crossover_point:]
            del population[pop_count].genes[crossover_point:]
            l2 = population[pop_count + 1].genes[crossover_point:]
            del population[pop_count + 1].genes[crossover_point:]

            population[pop_count].genes.extend(l2)
            population[pop_count + 1].genes.extend(l1)

            pop_count += 2
            break
        pop_count += 2

    return population


def mutation(population):
    for pop_count in range(individual.population_number):
        for gene_count in range(individual.number_of_genes):
            if gene_count % (rule.Rule.numberOfConditions + 1) == 0:
                if mutation_rate * 100 > random.randint(0, 100):
                    if population[pop_count].genes[gene_count] == 1:
                        population[pop_count].genes[gene_count] = 0
                    else:
                        population[pop_count].genes[gene_count] = 1
            else:
                if mutation_rate * 100 > random.randint(0, 100):
                    if population[pop_count].genes[gene_count] == 0:
                        if random.randint(0, 1) == 1:
                            population[pop_count].genes[gene_count] = 1
                        else:
                            population[pop_count].genes[gene_count] = 2
                    elif population[pop_count].genes[gene_count] == 1:
                        if random.randint(0, 1) == 1:
                            population[pop_count].genes[gene_count] = 0
                        else:
                            population[pop_count].genes[gene_count] = 2
                    elif population[pop_count].genes[gene_count] == 2:
                        if random.randint(0, 1) == 1:
                            population[pop_count].genes[gene_count] = 0
                        else:
                            population[pop_count].genes[gene_count] = 1

    return population
