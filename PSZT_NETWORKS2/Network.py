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
        self.graph.add_edge(index1, index2, capacity=toCapacity, systems=(toCapacity//self.modularity))

    def addDemand(self, id, capacity, paths):
        demand = Demand(id, capacity)
        for path in paths:
            demand.addPath(path)
        self.demands.append(demand)

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
                G.addNode(val)

        edges = []
        for child in root[0][1]:  # ta petla wczytuje krawedzie
            G.addEdge(child[0].text, child[1].text, 0)
            edges.append([G.cities.index(child[0].text), G.cities.index(child[1].text)])
            for key, val in child.attrib.items():
                G.linkIDs.append(val)

        sciezki = []
        sciezka = []
        for child in root[1]:  # tutaj wczytujemy zapotrzebowania i sciezki
            del sciezki[:]
            for links in child[3]:
                sciezka.clear()
                for link in links:
                    sciezka.append(edges[G.linkIDs.index(link.text)])
                sciezki.append(sciezka.copy())

            for key, val in child.attrib.items():
                G.addDemand(val, child[2].text, sciezki)
        return G

#G = Network(5)
#G.readNetwork()
#print("DEMANDS: ")

#G.printDemands()
#G.printNodes()
#G.printEdges()