import unittest


class MyQueue:
    data = []

    def is_empty(self):
        return self.data == []

    def add(self, record):
        self.data.insert(0, record)

    def remove(self):
        return None if self.is_empty() else self.data.pop()

    def size(self):
        return len(self.data)


class QueueTest(unittest.TestCase):
    def test_add(self):
        try:
            queue = MyQueue()
            queue.add(1)
        except Exception:
            self.fail("raised exception", Exception)

    def test_remove(self):
        try:
            queue = MyQueue()
            queue.add(1)
            queue.remove()
        except Exception:
            self.fail("raised exception", Exception)

    def test_order_of_elements(self):
        q = MyQueue()
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(1, q.remove())
        self.assertEqual(2, q.remove())
        self.assertEqual(3, q.remove())
        self.assertEqual(None, q.remove())
