import unittest


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        node = Node(data, self.head)
        self.head = node


class TestLinkedList(unittest.TestCase):
    def test_insert_first(self):
        linked_list = LinkedList()
        linked_list.insert_first(1)
        self.assertEqual(1, linked_list.head.data)
        linked_list.insert_first(2)
        self.assertEqual(2, linked_list.head.data)
