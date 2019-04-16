import unittest

class Node():
    def __init__(self, data, left = None, right = None):
        self.element = data
        self.left = left
        self.right = right

#O(n)
def preorder_traversal(start : Node):
    visited = []
    def recur(node: Node):
        nonlocal visited
        visited.append(node.element)
        if node.left:
            recur(node.left)
        if node.right:
            recur(node.right)

    recur(start)
    return visited

class Test(unittest.TestCase):
    def test_simple(self):
        head = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f', Node('g', None, Node('h')))))
        orderVisited = preorder_traversal(head)

        self.assertEqual(orderVisited[0], 'a')
        self.assertEqual(orderVisited[1], 'b')
        self.assertEqual(orderVisited[2], 'd')
        self.assertEqual(orderVisited[3], 'e')
        self.assertEqual(orderVisited[4], 'c')
        self.assertEqual(orderVisited[5], 'f')
        self.assertEqual(orderVisited[6], 'g')
        self.assertEqual(orderVisited[7], 'h')

if __name__ == "__main__":
    unittest.main()
