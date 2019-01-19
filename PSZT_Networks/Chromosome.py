import random
from Demand import Demand

class Chromosome(object):
    chrom = []

    def __init__(self):
        self.chrom = []

    def generate_random(self, demands):
        random.seed()
        for d in demands:
            pom = []
            cap = int(float(d.capacity))
            paths = d.paths
            for path in paths:
                rand = random.randint(0,cap)
                cap -= rand
                pom.append(rand)
            random.shuffle(pom)
            print(pom)
            self.chrom.append(pom)
