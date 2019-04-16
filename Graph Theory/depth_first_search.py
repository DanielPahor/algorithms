import unittest
import collections

class Node():
    def __init__(self, data):
        self.element = data
        self.children = []

#O(n+m)
def depth_first_search(start : Node):
    visited = collections.OrderedDict();

    def recur(node: Node, visited):
        visited[node.element] = True
        for child in node.children:
            if not child.element in visited:
                recur(child, visited)

    recur(start, visited)

    return visited

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
        node4.children = [node2, node3, node5]
        node5.children = [node4]

        visited = depth_first_search(node1);

        visitedIter = iter(visited)

        self.assertEqual(next(visitedIter), 'a')
        self.assertEqual(next(visitedIter), 'b')
        self.assertEqual(next(visitedIter), 'c')
        self.assertEqual(next(visitedIter), 'd')
        self.assertEqual(next(visitedIter), 'e')

if __name__ == "__main__":
    unittest.main()
