import random
from Demand import Demand
from Network import Network
import math


class Chromosome(object):
    chrom = []

    def __init__(self, chrom, network):
        self.chrom = chrom
        self.network = network

    def generate_random(self, demands):
        random.seed()
        for d in demands:
            pom = []
            cap = int(float(d.capacity))
            paths = d.paths
            for path in paths:
                rand = random.randint(0, cap)
                cap -= rand
                pom.append(rand)
            random.shuffle(pom)
            #print(pom)
            self.chrom.append(pom)

    def number_of_visits(self):
        edges = []
        for i in range (self.network.graph.number_of_edges()):
            edges.append(0)

        for demand in range(len(self.chrom)):
            for path in self.network.demands[demand].paths:
                    for edge in path:
                        if edges[self.network.findIndex(int(edge[0]), int(edge[1]))] < float(self.network.demands[i].capacity):
                            edges[self.network.findIndex(int(edge[0]), int(edge[1]))] = float(self.network.demands[i].capacity)

        numberOfSystems = 0
        for i in edges:
            numberOfSystems += math.ceil(i/self.network.modularity)

        return numberOfSystems


    def printBestConfig(self):
        edges = []
        for i in range(self.network.graph.number_of_edges()):
            edges.append(0)

        for i in range(len(self.chrom)):
            for j in range(len(self.chrom[i])):
                for path in self.network.demands[i].paths:
                    for edge in path:
                        edges[edge[0]] += self.chrom[i][j]
                        edges[edge[1]] += self.chrom[i][j]







    def __lt__(self, other):
        return self.number_of_visits() < other.number_of_visits()

    def cross(self, other):
        cross_point = int(len(self.chrom)/2)
        pom1 = []
        pom2 = []
        for i in range(0, cross_point):
            pom1.append(self.chrom[i])
            pom2.append(other.chrom[i])
        for i in range(cross_point, len(self.chrom)):
            pom1.append(other.chrom[i])
            pom2.append(self.chrom[i])

        result1 = Chromosome(pom1, self.network)
        result2 = Chromosome(pom2, self.network)

        if result1 < result2:
            return result1
        else:
            return result2


    def mutate(self, mutation_chance=5):
        random.seed()
        if random.randrange(0, 100) < mutation_chance:
            choice = random.randint(0, len(self.chrom)-1)
            cap = sum(self.chrom[choice])
            for i in range(0, len(self.chrom[choice])):
                rand = random.randint(0, cap)
                self.chrom[choice][i] = rand
            random.shuffle(self.chrom[choice])