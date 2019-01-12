import unittest


def validate(node, min=None, max=None):
    if max is not None and node.data > max:
        return False
    if min is not None and node.data < min:
        return False

    if node.left is not None and not validate(node.left, min, node.data):
        return False

    if node.right is not None and not validate(node.right, node.data, max):
        return False

    return True


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


class ValidateTest(unittest.TestCase):
    def test_should_return_true(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)

        self.assertTrue(validate(n))

    def test_should_return_false(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)
        n.left.left.right = Node(999)

        self.assertFalse(validate(n))
