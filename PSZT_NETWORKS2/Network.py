import networkx as nx
import xml.etree.ElementTree as ET
from Demand import Demand
#from Chromosome import Chromosome

class Network(object):
    modularity = 1
    cities = []         # Additional table for cities required since edges are represent by cities' names in UML and by indexex in nx.Graph.
    demands = []
    linkIDs = []
    graph = nx.Graph()

    def __init__(self, toModularity):
        self.modularity = toModularity

    def addNode(self, city):
        self.cities.append(city)
        self.graph.add_node(self.graph.number_of_nodes(), name=city)

    def addEdge(self, city1, city2, toCapacity):
        index1 = self.cities.index(city1)
        index2 = self.cities.index(city2)
        self.graph.add_edge(index1, index2, c1 = index1, c2 = index2, capacity=toCapacity, systems=(toCapacity//self.modularity))

    def addDemand(self, id, capacity, paths):
        demand = Demand(id, capacity)
        for path in paths:
            demand.addPath(path)
        self.demands.append(demand)

    def findIndex(self, index1, index2):
        counter = 0
        for edge in self.graph.edges:
            if edge[0] == index1 and edge[1]==index2:
                return counter
            counter += 1

    def printNodes(self):           # Not good looking, but necessary to print details of every node
        for i in range(self.graph.number_of_nodes()):
            print(i, self.graph.nodes[i])

    def printEdges(self):           # Not good looking, but necessary to print details of every edge
        for edge in self.graph.edges:
            print(edge, self.graph.edges[edge])

    def printDemands(self):
        for demand in self.demands:
            print(demand)

    def readNetwork(self):
        tree = ET.parse('polska.xml')
        root = tree.getroot()

        for child in root[0][0]:  # t petla wczytuje miasta
            for key, val in child.attrib.items():
                self.addNode(val)

        edges = []
        for child in root[0][1]:  # ta petla wczytuje krawedzie
            self.addEdge(child[0].text, child[1].text, 0)
            edges.append([self.cities.index(child[0].text), self.cities.index(child[1].text)])
            for key, val in child.attrib.items():
                self.linkIDs.append(val)

        sciezki = []
        sciezka = []
        for child in root[1]:  # tutaj wczytujemy zapotrzebowania i sciezki
            del sciezki[:]
            for links in child[3]:
                sciezka.clear()
                for link in links:
                    sciezka.append(edges[self.linkIDs.index(link.text)])
                sciezki.append(sciezka.copy())

            for key, val in child.attrib.items():
                self.addDemand(val, child[2].text, sciezki)
        return self

#G = Network(5)
#G.readNetwork()
#print("DEMANDS: ")

#G.printDemands()
#G.printNodes()
#G.printEdges()