import Network as Network
import Chromosome as Chromosome

# Main loop template
# Petle wykonujemy, dopoki najlepszy wynik nie bedzie sie roznil o mniej niz EPSILON w MAX_SMALL_INCREASE probach pod rzad...
# ... lub petla wykona sie juz MAX_REPEATS razy

last_result = 0 # Tutaj trzymac bedziemy ostatni wynik
epsilon = 0.1
max_small_increase = 5
current_small_increase = 0
max_repeats = 100
counter = 0 # Licznik obiegow petli
population = []
population_size = 2
modularity = 0
mutation_chance = 5

def generateStartPopulation(network):
    new_population = []
    for x in range(0, population_size):
        Ch = Chromosome()
        Ch.generate_random(network.demands)
        new_population.append(Ch)
    return new_population

def countBestResult(population):
        results = []
        for spec in population:
            results.append(spec.number_of_visits())
        return min(results)

def cross(population):
    i = 0
    children = []
    while i < len(population) - 1:
        children.append(population[i].cross(population[i+1]))
        i += 1
    new_population = population + children
    new_population.sort()
    new_population = new_population[:population_size]
    return new_population

def mutate(population):
    for spec in population:
        spec.mutate(mutation_chance)

def selectNewPopulation(population):
    mutate(population)
    return cross(population)

modularity = readModularity()
network = Network(modularity)
population = generateStartPopulation(network)

while True:
    best_result = countBestResult(population)

    if(counter == max_repeats):
        printResult(best_result)

    if(abs(best_result - last_result) <= epsilon):
        current_small_increase += 1

    if(current_small_increase == max_small_increase):
        printResult(best_result)
        break

    population = selectNewPopulation(population)
    counter += 1




