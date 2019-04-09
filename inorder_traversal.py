import unittest

class Node():
    def __init__(self, data, left = None, right = None):
        self.element = data
        self.left = left
        self.right = right

def inorder_traversal(start : Node):
    visited = []
    def recur(node: Node):
        if node.left:
            recur(node.left)
        nonlocal visited
        visited.append(node.element)
        if node.right:
            recur(node.right)

    recur(start)
    return visited

class Test(unittest.TestCase):
    def test_simple(self):
        head = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f', Node('g', None, Node('h')))))
        orderVisited = inorder_traversal(head)

        self.assertEqual(orderVisited[0], 'd')
        self.assertEqual(orderVisited[1], 'b')
        self.assertEqual(orderVisited[2], 'e')
        self.assertEqual(orderVisited[3], 'a')
        self.assertEqual(orderVisited[4], 'g')
        self.assertEqual(orderVisited[5], 'h')
        self.assertEqual(orderVisited[6], 'f')
        self.assertEqual(orderVisited[7], 'c')

if __name__ == "__main__":
    unittest.main()
