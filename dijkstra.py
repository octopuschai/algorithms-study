graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'fin': 1
    },
    'b': {
        'a': 3,
        'fin': 5
    },
    'fin': {},
}

infinity = float('inf')

costs = {
    'a': 6,
    'b': 2,
    'fin': infinity,
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None,
}

processed = set()


def init(graph):
    costs = {}
    parents = {}
    for key, value in graph['start'].items():
        costs[key] = value
        parents[key] = 'start'
    costs['fin'] = infinity
    parents['fin'] = None


def get_lowest_cost_node(costs):
    lowest_node = None
    lowest = float('inf')
    for node, cost in costs.items():
        if node not in processed and cost < lowest:
            lowest = cost
            lowest_node = node
    return lowest_node


def dijkstra(graph):
    node = get_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.add(node)
        node = get_lowest_cost_node(costs)


class Graph(object):
    infinity = float('inf')

    def __init__(self, graph):
        self.graph = graph
        self.costs = {}
        self.parents = {}
        self.processed = set()
        self._bulid_data()

    def _bulid_data(self, ):
        for key, value in self.graph['start'].items():
            self.costs[key] = value
            self.parents[key] = 'start'
        self.costs['fin'] = self.infinity
        self.parents['fin'] = None

    def _get_lowest_cost_node(self, costs):
        lowest_node = None
        lowest = float('inf')
        for node, cost in self.costs.items():
            if node not in self.processed and cost < lowest:
                lowest = cost
                lowest_node = node
        return lowest_node

    def dijkstra(self, ):
        node = self._get_lowest_cost_node(self.costs)
        while node:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for neighbor in neighbors.keys():
                new_cost = cost + neighbors[neighbor]
                if new_cost < self.costs[neighbor]:
                    self.costs[neighbor] = new_cost
                    self.parents[neighbor] = node
            self.processed.add(node)
            node = self._get_lowest_cost_node(self.costs)
