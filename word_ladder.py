""" build word ladder graph """

from graph import Graph
from my_queue import MyQueue


def build_graph(filename):
    """ build word ladder graph from word file, return Graph instance """
    d = {}  # original word buckets dictionary
    g = Graph()
    with open(filename, encoding='utf-8') as fd:
        for line in fd:
            word = line.rstrip('\n')
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    for bucket_lists in d.values():
        for word1 in bucket_lists:
            for word2 in bucket_lists:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g


def bfs(graph, start):
    """ breadth first search """
    q = MyQueue()
    visited_id = set()  # avoid visit repeated
    v = graph.get_vertex(start)
    if v:
        visited_id.add(v.id)  # add start vertex
        # add v.nbr in queue
        for i in v.get_connections():
            q.add(i)
            visited_id.add(i.id)
    else:
        raise ValueError('Error! start vertex {start} is not in Graph.')
    while q:  # bfs traverse
        current_vert = q.pop()
        print(current_vert.id)  # print vertex id by bfs

        for i in current_vert.get_connections():
            if i.id not in visited_id:
                q.add(i)
                visited_id.add(i.id)
