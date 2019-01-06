import unittest


class Queue:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def add(self, record):
        self.data.insert(0, record)

    def remove(self):
        return None if self.is_empty() else self.data.pop()

    def size(self):
        return len(self.data)

    def peek(self):
        return None if self.is_empty() else self.data[len(self.data) - 1]

    def print(self):
        print(self.data)


def weave(source_one, source_two):
    q = Queue()
    while source_one.peek() is not None or source_two.peek() is not None:
        if source_one.peek() is not None:
            q.add(source_one.remove())

        if source_two.peek() is not None:
            q.add(source_two.remove())

    return q


class WeaveTest(unittest.TestCase):
    def test_peek(self):
        q = Queue()
        q.add(1)
        q.add(2)
        self.assertEqual(1, q.peek())
        self.assertEqual(1, q.peek())
        self.assertEqual(1, q.remove())
        self.assertEqual(2, q.remove())

    def test_weave(self):
        one = Queue()
        two = Queue()
        one.add(1)
        one.add(2)
        one.add(3)
        one.add(4)
        two.add('one')
        two.add('two')
        two.add('three')
        two.add('four')

        result = weave(one, two)
        self.assertEqual(1, result.remove())
        self.assertEqual('one', result.remove())
        self.assertEqual(2, result.remove())
        self.assertEqual('two', result.remove())
        self.assertEqual(3, result.remove())
        self.assertEqual('three', result.remove())
        self.assertEqual(4, result.remove())
        self.assertEqual('four', result.remove())
        self.assertEqual(None, result.remove())
