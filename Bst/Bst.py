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

    def contains(self, data):
        if self.data is data:
            return self
        if data < self.data and self.left is not None:
            return self.left.contains(data)
        elif data > self.data and self.right is not None:
            return self.right.contains(data)
        else:
            return None


class BstTest(unittest.TestCase):
    def test_insert(self):
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(17)

        self.assertEqual(5, node.left.data)
        self.assertEqual(15, node.right.data)
        self.assertEqual(17, node.right.right.data)

    def test_contains(self):
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(20)
        node.insert(0)
        node.insert(-5)
        node.insert(3)

        three = node.left.left.right
        self.assertEqual(three, node.contains(3))

    def test_should_return_none(self):
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(20)
        node.insert(0)
        node.insert(-5)
        node.insert(3)

        self.assertEqual(None, node.contains(9999))
