""" build word ladder graph """

from graph import Graph


def build_graph(filename):
    """ build word ladder graph from word file, return Graph instance """
    d = {}  # original word buckets dictionary
    g = Graph()
    with open(filename) as fd:
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
