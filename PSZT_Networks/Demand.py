class Demand(object):
    demand_id = 0
    capacity = 0
    paths =[]

    def __init__(self, id, capacity):
        self.demand_id = id
        self.capacity = capacity
        self.paths = []

    def __str__(self):
        return "ID: %s:, Capacity: %s, Admissable paths: %s" % (self.demand_id, self.capacity, self.paths)

    def addPath(self, links):
        self.paths.append(links)


