import unittest


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        self.insert_at(data, 0)

    def size(self):
        size = 0
        node = self.head
        while node is not None:
            size = size + 1
            node = node.next_node
        return size

    def get_first(self):
        return self.get_at(0)

    def get_last(self):
        return self.get_at(self.size() - 1)

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
        self.insert_at(data, self.size())

    def get_at(self, index):
        if index >= self.size() or index < 0 or self.head is None:
            return None
        else:
            node = self.head
            counter = 0
            while counter < index:
                node = node.next_node
                counter = counter + 1
            return node

    def remove_at(self, index):
        if self.size() is 0:
            return
        elif index is 0:
            self.head = self.head.next_node
        elif 0 < index < self.size():
            counter = 0
            previous_node = self.get_at(index - 1)
            previous_node.next_node = previous_node.next_node.next_node

    def insert_at(self, data, index):
        new_node = Node(data)
        if self.size() == 0:
            self.head = new_node
        elif index <= 0:
            new_node.next_node = self.head
            self.head = new_node
        elif index >= self.size():
            last_node = self.get_last()
            last_node.next_node = new_node
        else:
            previous_node = self.get_at(index - 1)
            new_node.next_node = previous_node.next_node
            previous_node.next_node = new_node


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

    def test_get_at(self):
        linked_list = LinkedList()
        self.assertEqual(None, linked_list.get_at(10))

        linked_list.insert_last(1)
        linked_list.insert_last(2)
        linked_list.insert_last(3)
        linked_list.insert_last(4)

        self.assertEqual(1, linked_list.get_at(0).data)
        self.assertEqual(2, linked_list.get_at(1).data)
        self.assertEqual(3, linked_list.get_at(2).data)
        self.assertEqual(4, linked_list.get_at(3).data)

    def test_remove_at_with_empty_list(self):
        try:
            linked_list = LinkedList()
            linked_list.remove_at(0)
            linked_list.remove_at(1)
            linked_list.remove_at(2)
        except Exception:
            self.fail("raised exception", Exception)

    def test_remove_at_on_an_index_out_of_bounds(self):
        try:
            linked_list = LinkedList()

            linked_list.insert_last('a')
            linked_list.remove_at(1)
        except Exception:
            self.fail("raised exception", Exception)

    def test_remove_at_with_first_node(self):
        linked_list = LinkedList()

        linked_list.insert_last(1)
        linked_list.insert_last(2)
        linked_list.insert_last(3)
        linked_list.insert_last(4)
        self.assertEqual(1, linked_list.get_at(0).data)
        linked_list.remove_at(0)
        self.assertEqual(2, linked_list.get_at(0).data)

    def test_remove_at_with_index(self):
        linked_list = LinkedList()
        linked_list.insert_last(1)
        linked_list.insert_last(2)
        linked_list.insert_last(3)
        linked_list.insert_last(4)
        self.assertEqual(2, linked_list.get_at(1).data)
        linked_list.remove_at(1)
        self.assertEqual(3, linked_list.get_at(1).data)

    def test_remove_at_with_last_node(self):
        linked_list = LinkedList()
        linked_list.insert_last(1)
        linked_list.insert_last(2)
        linked_list.insert_last(3)
        linked_list.insert_last(4)
        self.assertEqual(4, linked_list.get_at(3).data)
        linked_list.remove_at(3);
        self.assertEqual(None, linked_list.get_at(3))

    def test_insert_at_with_adding_at_the_zero_index_of_empty_list(self):
        linked_list = LinkedList()
        linked_list.insert_at('hi', 0)
        self.assertEqual('hi', linked_list.get_first().data)

    def test_insert_at_with_adding_at_the_zero_index_of_nonempty_list(self):
        linked_list = LinkedList()
        linked_list.insert_last('a')
        linked_list.insert_last('b')
        linked_list.insert_last('c')
        linked_list.insert_at('hi', 0)
        self.assertEqual('hi', linked_list.get_at(0).data)
        self.assertEqual('a', linked_list.get_at(1).data)
        self.assertEqual('b', linked_list.get_at(2).data)
        self.assertEqual('c', linked_list.get_at(3).data)

    def test_insert_at_with_adding_data_at_a_middle_index(self):
        linked_list = LinkedList()
        linked_list.insert_last('a')
        linked_list.insert_last('b')
        linked_list.insert_last('c')
        linked_list.insert_last('d')
        linked_list.insert_at('hi', 2)
        self.assertEqual('a', linked_list.get_at(0).data)
        self.assertEqual('b', linked_list.get_at(1).data)
        self.assertEqual('hi', linked_list.get_at(2).data)
        self.assertEqual('c', linked_list.get_at(3).data)
        self.assertEqual('d', linked_list.get_at(4).data)

    def test_insert_at_with_adding_data_at_last_index(self):
        linked_list = LinkedList()
        linked_list.insert_last('a')
        linked_list.insert_last('b')
        linked_list.insert_at('hi', 2)
        self.assertEqual('a', linked_list.get_at(0).data)

    def test_insert_at_with_adding_new_node_with_out_of_bound_index(self):
        linked_list = LinkedList()

        linked_list.insert_last('a')
        linked_list.insert_last('b')
        linked_list.insert_at('hi', 30)

        self.assertEqual('a', linked_list.get_at(0).data)
        self.assertEqual('b', linked_list.get_at(1).data)
        self.assertEqual('hi', linked_list.get_at(2).data)
