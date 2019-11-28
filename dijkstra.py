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

graph2 = {
    'start': {
        'a': 5,
        'b': 0
    },
    'a': {
        'c': 15,
        'd': 20
    },
    'b': {
        'c': 30,
        'd': 35
    },
    'c': {
        'fin': 20
    },
    'd': {
        'fin': 10
    },
    'fin': {}
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
    for key, value in graph.items():
        if key == 'start':
            for node, cost in graph['start'].items():
                costs[node] = cost
                parents[node] = 'start'
        else:
            if key not in costs:
                costs[key] = infinity
                parents[key] = None


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
        self.graph = graph  # 原始DAG图
        self.costs = {}  # 保存节点开销
        self.parents = {}  # 保存父节点
        self.processed = set()  # 记录处理过的节点
        self._bulid_data()

    def _bulid_data(self, ):
        """ 根据graph，构造初始costs和parents """
        for key, value in self.graph.items():
            if key == 'start':
                for node, cost in self.graph['start'].items():
                    self.costs[node] = cost
                    self.parents[node] = 'start'
            else:
                if key not in self.costs:
                    self.costs[key] = self.infinity
                    self.parents[key] = None

    def _get_lowest_cost_node(self, costs):
        """ 遍历graph图，获取最小开销的节点 """
        lowest_node = None
        lowest = float('inf')
        for node, cost in self.costs.items():
            if node not in self.processed and cost < lowest:
                lowest = cost
                lowest_node = node
        return lowest_node

    def dijkstra(self, ):
        """ dijkstra算法 """
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

    def route(self, end='fin'):
        """ 显示起点到各节点的最短路径，默认是到终点的最短路径 """
        p_node = self.parents[end]
        shortest_route = ''
        while p_node != 'start':
            shortest_route = f'-->({p_node})' + shortest_route
            p_node = self.parents[p_node]
        return f'shortest route: (start){shortest_route}-->({end})'
