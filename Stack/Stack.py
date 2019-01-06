import unittest


class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def push(self, record):
        self.data.append(record)

    def pop(self):
        return None if self.is_empty() else self.data.pop()

    def peek(self):
        return None if self.is_empty() else self.data[len(self.data) - 1]

    def print(self):
        print(self.data)


class StackTest(unittest.TestCase):
    def test_add_remove(self):
        s = Stack()
        s.push(1)
        self.assertEqual(1, s.pop())
        s.push(2)
        self.assertEqual(2, s.pop())

    def test_last_in_first_out(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(3, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())

    def test_peek(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(3, s.peek())
        self.assertEqual(3, s.pop())
        self.assertEqual(2, s.peek())
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.peek())
        self.assertEqual(1, s.pop())
