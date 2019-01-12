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


class Tree:
    def __init__(self):
        self.root = None

    def traverse_bf(self, test_arr):
        arr = [self.root]
        while len(arr) > 0:
            node = arr.pop(0)

            for child in node.children:
                arr.append(child)
            test_arr.append(node.data)


class NodeTest(unittest.TestCase):
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


class TreeTest(unittest.TestCase):
    def test_should_start_empty(self):
        t = Tree()
        self.assertEqual(None, t.root)

    def test_traverse_bf(self):
        letters = []
        t = Tree()
        t.root = Node('a')
        t.root.add('b')
        t.root.add('c')
        t.root.children[0].add('d')

        t.traverse_bf(letters)

        self.assertEqual(['a', 'b', 'c', 'd'], letters)
