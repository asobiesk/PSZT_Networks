from Network import Network
from Chromosome import Chromosome

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
       #print("Current best: ", best.number_of_visits())
       for spec in population:
           #print("current spec: ", spec.number_of_visits())
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
    print("Sciezki: ")
    print(result.chrom)



#main function

#modularity = readModularity()
print("ZAczyanm")
modularity = 100
network = Network(modularity)
network.readNetwork()
print("")
population = generateStartPopulation(network)

print(population[0].chrom)
print(population[1].chrom)
print("NAJLEPSZY WYNIK W RANDOMIE: ")
#zajebioza = countBestUnit(population)
#print(zajebioza.number_of_visits())
print("PETLA")
network.printNodes()
network.printEdges()
network.printDemands()
while True:
    print("W petli")
    best_unit = countBestUnit(population)
    best_result = best_unit.number_of_visits()

    if(counter == max_repeats):
        printResult(best_unit)
        break

    if(abs(best_result - last_result) <= epsilon):
        current_small_increase += 1

    if(current_small_increase == max_small_increase):
        printResult(best_unit)
        break

    print("Obieg: ", counter)
    print("Wynik: ", best_result)
    population = selectNewPopulation(population)
    counter += 1

print("Skonczylem")


