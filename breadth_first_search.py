import unittest

class Node():
    def __init__(self, data):
        self.element = data
        self.children = []

def breadth_first_search(nodes, start : Node):
    visited = {}
    for node in nodes:
        visited[node] = False
    visited[start] = True

    layers, currentLayer, nextLayer = [], [start], []

    while currentLayer:
        for node in currentLayer:
            for neighbour in node.children:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    nextLayer.append(neighbour)
        layers.append(currentLayer)
        currentLayer, nextLayer = nextLayer, []

    return layers

class Test(unittest.TestCase):
    def test_simple(self):
        node1 = Node('a')
        node2 = Node('b')
        node3 = Node('c')
        node4 = Node('d')
        node5 = Node('e')

        node1.children = [node2, node3]
        node2.children = [node1, node3, node4]
        node3.children = [node1, node2, node4]
        node4.children = [node3, node2, node5]
        node5.children = [node4]

        layers = breadth_first_search([node1, node2, node3, node4, node5], node1);

        self.assertEqual(layers[0][0], node1)
        self.assertEqual(layers[1][0], node2)
        self.assertEqual(layers[1][1], node3)
        self.assertEqual(layers[2][0], node4)
        self.assertEqual(layers[3][0], node5)

if __name__ == "__main__":
    unittest.main()
