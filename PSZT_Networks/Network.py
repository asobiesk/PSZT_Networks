import networkx as nx
from Demand import Demand

class Network(object):
    modularity = 1
    cities = []         #Additional table for cities required since edges are represent by cities' names in UML and by indexex in nx.Graph.
    demands = []
    graph = nx.Graph()

    def __init__(self, toModularity):
        self.modularity = toModularity

    def addNode(self, city):
        self.cities.append(city)
        self.graph.add_node(self.graph.number_of_nodes(), name=city)

    def addEdge(self, city1, city2, toCapacity):
        index1 = self.cities.index(city1)
        index2 = self.cities.index(city2)
        self.graph.add_edge(index1, index2, capacity=toCapacity, systems=(toCapacity//self.modularity))

    def addDemand(self, id, capacity, paths):
        demand = Demand(id, capacity)
        for path in paths:
            demand.addPath(path)
        self.demands.append(demand)

    def printNodes(self):           #Not good looking, but necessary to print detalis of every node
        for i in range(self.graph.number_of_nodes()):
            print(i, self.graph.nodes[i])

    def printEdges(self):           #Not good looking, but necessary to print detalis of every edge
        for edge in self.graph.edges:
            print(edge, self.graph.edges[edge])

    def printDemands(self):
        for demand in self.demands:
            print(demand)

    def readNetwork(self):
        #To be done
        1==1;   #Some NOP for avoiding errors

#same sample code for test purposes
G = Network(5)
G.addNode('Warszawa')
G.addNode('Plock')
G.addNode('Krakow')
G.printNodes()

G.addEdge('Warszawa', 'Plock', 10)
G.addEdge('Plock', 'Krakow', 17)
G.addEdge('Krakow', 'Warszawa', 7)
G.printEdges()


toLinks1 = [[0,1], [1,2]]
toLinks2 = [[0,2]]
paths = []
paths.append(toLinks1)
paths.append(toLinks2)

G.addDemand('demand0_2', 50, paths)
print("DEMANDS: ")
G.printDemands()
