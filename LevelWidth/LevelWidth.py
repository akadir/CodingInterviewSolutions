import unittest


def level_width(root):
    arr = [root, 's']
    counters = [0]

    while len(arr) > 1:
        node = arr.pop(0)

        if node is 's':
            counters.append(0)
            arr.append('s')
        else:
            arr = arr + node.children
            counters[len(counters) - 1] = counters[len(counters) - 1] + 1

    return counters


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        node = Node(data)
        self.children.append(node)

    def remove(self, data):
        self.children = [n for n in self.children if n.data is not data]


class LevelWidthTest(unittest.TestCase):
    def test_level_width(self):
        root = Node(0)
        root.add(1)
        root.add(2)
        root.add(3)
        root.children[0].add(4)
        root.children[2].add(5)

        self.assertEqual([1, 3, 2], level_width(root))

        root = Node(0)
        root.add(1)
        root.children[0].add(2)
        root.children[0].add(3)
        root.children[0].children[0].add(4)

        self.assertEqual([1, 1, 2, 1], level_width(root))
