import unittest

class Node():
    def __init__(self, data, left = None, right = None):
        self.element = data
        self.left = left
        self.right = right

def postorder_traversal(start : Node):
    visited = []
    def recur(node: Node):
        if node.left:
            recur(node.left)
        if node.right:
            recur(node.right)
        nonlocal visited
        visited.append(node.element)

    recur(start)
    return visited

class Test(unittest.TestCase):
    def test_simple(self):
        head = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f', Node('g', None, Node('h')))))
        orderVisited = postorder_traversal(head)

        self.assertEqual(orderVisited[0], 'd')
        self.assertEqual(orderVisited[1], 'e')
        self.assertEqual(orderVisited[2], 'b')
        self.assertEqual(orderVisited[3], 'h')
        self.assertEqual(orderVisited[4], 'g')
        self.assertEqual(orderVisited[5], 'f')
        self.assertEqual(orderVisited[6], 'c')
        self.assertEqual(orderVisited[7], 'a')

if __name__ == "__main__":
    unittest.main()
