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

    def size(self):
        size = 0
        node = self.head
        while node is not None:
            size = size + 1
            node = node.next_node
        return size

    def get_first(self):
        return self.head

    def get_last(self):
        last = self.head
        while last is not None and last.next_node is not None:
            last = last.next_node
        return last

    def clear(self):
        self.head = None

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next_node


class TestLinkedList(unittest.TestCase):
    def test_insert_first(self):
        linked_list = LinkedList()
        linked_list.insert_first(1)
        self.assertEqual(1, linked_list.head.data)
        linked_list.insert_first(2)
        self.assertEqual(2, linked_list.head.data)

    def test_size(self):
        linked_list = LinkedList()
        self.assertEqual(0, linked_list.size())
        linked_list.insert_first(1)
        linked_list.insert_first(1)
        linked_list.insert_first(1)
        linked_list.insert_first(1)
        self.assertEqual(4, linked_list.size())

    def test_get_first(self):
        linked_list = LinkedList()
        linked_list.insert_first(1)
        self.assertEqual(1, linked_list.get_first().data)
        linked_list.insert_first(2)
        self.assertEqual(2, linked_list.get_first().data)

    def test_get_last(self):
        linked_list = LinkedList()
        linked_list.insert_first(2)
        self.assertEqual(2, linked_list.get_last().data)
        self.assertEqual(None, linked_list.get_last().next_node)
        linked_list.insert_first(1)
        self.assertEqual(2, linked_list.get_last().data)
        self.assertEqual(None, linked_list.get_last().next_node)

    def test_clear(self):
        linked_list = LinkedList()
        self.assertEqual(0, linked_list.size())
        linked_list.insert_first(1)
        linked_list.insert_first(1)
        linked_list.insert_first(1)
        linked_list.insert_first(1)
        self.assertEqual(4, linked_list.size())
        linked_list.clear()
        self.assertEqual(0, linked_list.size())

    def test_remove_first(self):
        linked_list = LinkedList()
        linked_list.insert_first('a')
        linked_list.remove_first()
        self.assertEqual(0, linked_list.size())
        self.assertEqual(None, linked_list.get_first())

    def test_remove_first_when_list_has_size_of_three(self):
        l = LinkedList()
        l.insert_first('c')
        l.insert_first('b')
        l.insert_first('a')
        l.remove_first()
        self.assertEqual(2, l.size())
        self.assertEqual('b', l.get_first().data)
        l.remove_first()
        self.assertEqual(1, l.size())
        self.assertEqual('c', l.get_first().data)
