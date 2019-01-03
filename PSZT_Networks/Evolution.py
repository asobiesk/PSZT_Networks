import Network as Network

#Main loop template
#Petle wykonujemy, dopoki najlepszy wynik nie bedzie sie roznil o mniej niz EPSILON w MAX_SMALL_INCREASE probach pod rzad...
#... lub petla wykona sie juz MAX_REPEATS razy

last_result = 0 #Tutaj trzymac bedziemy ostatni wynik
epsilon = 0.1
max_small_increase = 5
current_small_increase = 0
max_repeats = 100
counter = 0 #Licznik obiegow petli
population = []
modularity = 0



population = generateStartPopulation()
modularity = readModularity()
network = Network(modularity)

while True:
    best_result = countBestResult()

    if(counter == max_repeats):
        printResult(best_result)

    if(abs(best_result - last_result) <= epsilon):
        current_small_increase += 1

    if(current_small_increase == max_small_increase):
        printResult(best_result)
        break

    cross()
    mutate()
    population = selectNewPopulation()
    counter += 1




