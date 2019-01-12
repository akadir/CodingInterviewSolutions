import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        node = Node(data)
        self.children.append(node)


class TreeTest(unittest.TestCase):
    def test_create_node(self):
        n = Node('a')
        self.assertEqual('a', n.data)
        self.assertEqual(0, len(n.children))

    def test_add_node(self):
        n = Node('a')
        n.add('b')
        self.assertEqual(1, len(n.children))
        self.assertEqual([], n.children[0].children)
