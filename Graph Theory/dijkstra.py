import unittest
import collections

class Node():
    def __init__(self, data):
        self.element = data
        self.children = []

# to-do: use priority queue
# to-do: tests
# to-do: return path and cost

#O(V^2 + E) = O(V^2)
def dijkstra(start, nodes):
    distance = {}
    previous = {}

    for node in nodes:
        distance[node] = None
        previous[node] = None
    distance[start] = 0

    while nodes:
        min = get_min(nodes, distance)

        for neighbour in min.children:
            new_distance = distance(current) + get_edge_cost(neighbour)
            if new_distance < distance[neighbour]:
                distace[neighbour] = new_distance
                previous[neighbour] = min

        nodes.remove(min)

def get_edge_cost(node):
    return node[1]

def get_min(nodes, distance):
    smallest = distance(nodes[0])

    for node in nodes:
        if distance(node) < smallest:
            smallest = node
    return smallest


class Test(unittest.TestCase):
    def test_simple(self):

        self.assertEqual(next(visitedIter), 'e')

if __name__ == "__main__":
    unittest.main()
