class Vertex(object):
    """ vertex is a node in graph """
    def __init__(self, key):
        self.id = key
        self.connect_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connect_to[nbr] = weight

    def __str__(self, ):
        return f'{self.id} connect to: {str([x for x in self.connect_to])}'

    def get_connections(self, ):
        return self.connect_to.keys()

    def get_id(self, ):
        return self.id

    def get_weight(self, nbr):
        return self.connect_to[nbr]


class Graph(object):
    def __init__(self, ):
        self.vertices_list = {}
        self.vertices_num = 0

    def add_vertex(self, key):
        new_vert = Vertex(key)
        self.vertices_list[key] = new_vert
        self.vertices_num += 1
        return new_vert

    def add_edge(self, from_id, to_id, weight=0):
        if from_id not in self.vertices_list:
            self.add_vertex(from_id)
        if to_id not in self.vertices_list:
            self.add_vertex(to_id)
        self.vertices_list[from_id].add_neighbor(to_id, weight)

    def get_vertex(self, key):
        if key in self.vertices_list:
            return self.vertices_list[key]

    def get_vertices(self, ):
        return self.vertList.keys()

    def __contains__(self, key):
        return key in self.vertices_list

    def __iter__(self, ):
        return iter(self.vertices_list.values())


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for w in v.get_connections():
            print(f'({v.get_id()}, {w})')
