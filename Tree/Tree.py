import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        node = Node(data)
        self.children.append(node)

    def remove(self, data):
        self.children = [n for n in self.children if n.data is not data]
        # for d in self.children:
        #     if d.data is data:
        #         self.children.remove(d)


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

    def test_remove_node(self):
        n = Node('a')
        n.add('b')
        self.assertEqual(1, len(n.children))
        n.remove('b')
        self.assertEqual(0, len(n.children))
