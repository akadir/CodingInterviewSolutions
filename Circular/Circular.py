import unittest


def circular(linked_list):
    slow = linked_list.head
    fast = linked_list.head

    while fast.next_node is not None and fast.next_node.next_node is not None:
        slow = slow.next_node
        fast = fast.next_node.next_node

        if slow is fast:
            return True

    return False


class CircularTest(unittest.TestCase):
    def test_should_return_true_with_circular_list(self):
        linked_list = LinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')

        linked_list.head = a
        a.next_node = b
        b.next_node = c
        c.next_node = b

        self.assertTrue(circular(linked_list))

        linked_list = LinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')

        linked_list.head = a
        a.next_node = b
        b.next_node = c
        c.next_node = a

        self.assertTrue(circular(linked_list))

    def test_should_return_false_with_circular_list(self):
        linked_list = LinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')

        linked_list.head = a
        a.next_node = b
        b.next_node = c
        c.next_node = None

        self.assertFalse(circular(linked_list))


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
