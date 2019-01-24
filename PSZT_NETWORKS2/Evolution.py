from Network import Network
from Chromosome import Chromosome
import random
import copy
import networkx as nx

import math
# Main loop template
# Petle wykonujemy, dopoki najlepszy wynik nie bedzie sie roznil o mniej niz EPSILON w MAX_SMALL_INCREASE probach pod rzad...
# ... lub petla wykona sie juz MAX_REPEATS razy

epsilon = 1
max_small_increase = 100
current_small_increase = 0
max_repeats = 100
counter = 0 # Licznik obiegow petli
population = []
population_size = 10
mutation_chance = 5
best_result = 0

def generateStartPopulation(network):
    new_population = []
    for x in range(0, population_size):
        Ch = Chromosome([], network)
        Ch.generate_random(network.demands)
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



####################################main function###########################################################
country = int(input("Ktora siec? [0]Polska [1]Stany Zjednoczone  "))
modularity = int(input("Podaj modularność grafu:  "))
option = int(input("Podaj opcję: [0] Przepustowości się nie sumują [1] Przepustowości się sumują  "))


network = Network(modularity, option, country)

network.readNetwork()
if(country != 0):
    print("Trwa generowanie sciezek...")
    network.addPaths()
    print("Wygenerowano sciezki")

print("")
population = generateStartPopulation(network)
last_result = float('inf')
bestResoultTillNow = countBestUnit(population)

while True:
    print("W petli")
    best_unit = countBestUnit(population)
    best_result = best_unit.number_of_visits()

    if (best_unit < bestResoultTillNow):
        bestResoultTillNow = copy.deepcopy(best_unit)

    if(counter == max_repeats):
        printResult(bestResoultTillNow)
        break



    if(abs(best_result - last_result) <= epsilon):
        current_small_increase += 1
    else:
        current_small_increase = 0

    if(current_small_increase == max_small_increase):
        printResult(bestResoultTillNow)
        break

    print("Obieg: ", counter)
    print("Wynik: ", best_result)

    for i in population:
        print(i.chrom)

    if (last_result < best_result):
        printResult(bestResoultTillNow)
        break

    population = selectNewPopulation(population)
    counter += 1
    last_result = best_result
print("Skonczylem")



