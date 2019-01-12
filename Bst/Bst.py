import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data and self.left is not None:
            self.left.insert(data)
        elif data < self.data:
            self.left = Node(data)
        elif data >= self.data and self.right is not None:
            self.right.insert(data)
        elif data >= self.data:
            self.right = Node(data)


class BstTest(unittest.TestCase):
    def test_insert(self):
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(17)

        self.assertEqual(5, node.left.data)
        self.assertEqual(15, node.right.data)
        self.assertEqual(17, node.right.right.data)
