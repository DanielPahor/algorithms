import unittest
import collections
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, start_vertex):
        # start all distances at infinity, except the start node
        distances = {v:float('inf') for v in range(self.v)}
        distances[start_vertex] = 0

        # put the start node into the priority queue
        unvisited = PriorityQueue()
        unvisited.put((0, start_vertex))

        # while there are nodes to visit
        while not unvisited.empty():
            # get the current best distance to the node and mark it as visited
            (dist, current_vertex) = unvisited.get()
            self.visited.append(current_vertex)

            # look at all the nodes potential neighbors
            for neighbor in range(self.v):
                # if there is an edge between current and potential neighbour
                if self.edges[current_vertex][neighbor] != -1:
                    # get the distance to the neighbour from the current node
                    distance_to_neighbour = self.edges[current_vertex][neighbor]

                    # if the node has not been visited
                    if neighbor not in self.visited:
                        old_cost = distances[neighbor]
                        new_cost = distances[current_vertex] + distance_to_neighbour

                        # update it with the new shortest path, if appicable
                        if new_cost < old_cost:
                            unvisited.put((new_cost, neighbor))
                            distances[neighbor] = new_cost
                            # can record prev node here if want to

        # return the shortest path to all nodes
        return distances

class Test(unittest.TestCase):
    def test_simple(self):
        g = Graph(5)

        g.add_edge(0,1,6)
        g.add_edge(0,3,1)
        g.add_edge(1,0,6)
        g.add_edge(1,3,2)
        g.add_edge(1,2,5)
        g.add_edge(1,4,2)
        g.add_edge(2,1,5)
        g.add_edge(2,4,5)
        g.add_edge(3,0,1)
        g.add_edge(3,1,2)
        g.add_edge(3,4,1)
        g.add_edge(4,3,1)
        g.add_edge(4,1,2)
        g.add_edge(4,2,5)

        D = g.dijkstra(0)

        self.assertEqual(D[0], 0)
        self.assertEqual(D[1], 3)
        self.assertEqual(D[2], 7)
        self.assertEqual(D[3], 1)
        self.assertEqual(D[4], 2)

if __name__ == "__main__":
    unittest.main()
