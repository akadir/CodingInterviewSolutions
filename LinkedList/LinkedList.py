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

    def remove_last(self):
        size_of_linked_list = self.size()
        if size_of_linked_list is 0:
            return
        elif size_of_linked_list is 1:
            self.head = None
        else:
            previous = self.head
            last = self.head

            while last is not None and last.next_node is not None:
                previous = last
                last = last.next_node

            previous.next_node = None

    def insert_last(self, data):
        new_node = Node(data)
        last_node = self.get_last()
        if last_node is None:
            self.head = new_node
        else:
            last_node.next_node = new_node


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
        linked_list = LinkedList()
        linked_list.insert_first('c')
        linked_list.insert_first('b')
        linked_list.insert_first('a')
        linked_list.remove_first()
        self.assertEqual(2, linked_list.size())
        self.assertEqual('b', linked_list.get_first().data)
        linked_list.remove_first()
        self.assertEqual(1, linked_list.size())
        self.assertEqual('c', linked_list.get_first().data)

    def test_remove_last_with_empty_list(self):
        try:
            linked_list = LinkedList()
            linked_list.remove_last()
        except Exception:
            self.fail("raised exception", Exception)

    def test_remove_last_with_list_has_size_of_one(self):
        linked_list = LinkedList()
        linked_list.insert_first('a')
        linked_list.remove_last()
        self.assertEqual(None, linked_list.head)

    def test_remove_last_with_list_has_size_of_two(self):
        linked_list = LinkedList()
        linked_list.insert_first('b')
        linked_list.insert_first('a')

        linked_list.remove_last()

        self.assertEqual(1, linked_list.size())
        self.assertEqual('a', linked_list.head.data)

    def test_remove_last_with_list_has_size_of_three(self):
        linked_list = LinkedList()
        linked_list.insert_first('c')
        linked_list.insert_first('b')
        linked_list.insert_first('a')
        linked_list.remove_last()

        self.assertEqual(2, linked_list.size())
        self.assertEqual('b', linked_list.get_last().data)

    def test_insert_last(self):
        linked_list = LinkedList()
        linked_list.insert_first('a')

        linked_list.insert_last('b')

        self.assertEqual(2, linked_list.size())
        self.assertEqual('b', linked_list.get_last().data)
