from Network import Network
from Chromosome import Chromosome
import random
import math
# Main loop template
# Petle wykonujemy, dopoki najlepszy wynik nie bedzie sie roznil o mniej niz EPSILON w MAX_SMALL_INCREASE probach pod rzad...
# ... lub petla wykona sie juz MAX_REPEATS razy

last_result = 0 # Tutaj trzymac bedziemy ostatni wynik
epsilon = 1
max_small_increase = 100
current_small_increase = 0
max_repeats = 100
counter = 0 # Licznik obiegow petli
population = []
population_size = 5
mutation_chance = 5
best_result = 0

def generateStartPopulation(network):
    new_population = []
    for x in range(0, population_size):
        print("robie nowego randa")
        Ch = Chromosome([], network)
        Ch.generate_random(network.demands)
        print(Ch.chrom)
        new_population.append(Ch)
    return new_population

def countBestUnit(population):
       best = population[0]
       for spec in population:
           if spec.number_of_visits() < best.number_of_visits():
                best = spec
       return best

def cross(population):
    i = 0
    children = []
    while i < len(population) - 1:
        children.append(population[i].cross(population[i+1]))
        i += 1
    new_population = population + children
    new_population.sort()
    #random.shuffle(new_population)
    new_population = new_population[:population_size]
    return new_population

def mutate(population):
    for spec in population:
        spec.mutate(mutation_chance)

def selectNewPopulation(population):
    mutate(population)
    return cross(population)

def printResult(result):
    print("Wyniki: ")
    print("Minimalna znaleziona liczba wizyt: ")
    wynik = result.number_of_visits()
    print(wynik)
    print("Krawedzie: ")
    edges = result.returnBestConfig()
    i=0
    for krawedz in network.graph.edges:
        print(network.cities[krawedz[0]], network.cities[krawedz[1]], edges[i], math.ceil(edges[i]/network.modularity))
        i += 1



#main function

#modularity = readModularity()
print("ZAczyanm")
modularity = 100
network = Network(modularity)
network.readNetwork()
print("")
population = generateStartPopulation(network)
last_result = 0

while True:
    print("W petli")
    best_unit = countBestUnit(population)
    best_result = best_unit.number_of_visits()

    if(counter == max_repeats):
        printResult(best_unit)
        break

    if(abs(best_result - last_result) <= epsilon):
        current_small_increase += 1
    else:
        current_small_increase = 0

    if(current_small_increase == max_small_increase):
        printResult(best_unit)
        break

    print("Obieg: ", counter)
    print("Wynik: ", best_result)

    for i in population:
        print(i.chrom)

    population = selectNewPopulation(population)
    counter += 1
    last_result = best_result
print("Skonczylem")


