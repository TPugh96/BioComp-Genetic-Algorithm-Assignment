import rule
import data

dataSet = data.read_file()


def evaluate_fitness(population):
    for individual in population:
        individual.fitness = 0
        fitness_function(individual, dataSet)


def fitness_function(individual, data_set):
    gene_count = 0
    rule_base = []

    for new_rule in range(0, rule.numberOfRules):
        rule_base.append(rule.Rule())

        for condition in range(0, rule_base[new_rule].numberOfConditions):
            rule_base[new_rule].conditions.append(individual.genes[gene_count])
            gene_count += 1

        rule_base[new_rule].output = individual.genes[gene_count]
        gene_count += 1

    for current_data in data_set:
        for current_rule in rule_base:
            if rule.check_rules_match(current_data.bytes, current_rule.conditions):
                if current_data.output == current_rule.output:
                    individual.fitness += 1
                break

    return individual


def get_total_fitness(population):
    fitness = 0

    for individual in population:
        fitness += individual.fitness

    return fitness


def get_mean_fitness(population, population_size):
    mean_fitness = get_total_fitness(population) / population_size

    return mean_fitness
