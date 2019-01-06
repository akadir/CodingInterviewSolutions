import unittest


#
#
# class Stack:
#     data = []
#
#     def __init__(self):
#         self.data = []
#
#     def is_empty(self):
#         return self.data == []
#
#     def push(self, record):
#         self.data.append(record)
#
#     def pop(self):
#         return None if self.is_empty(self) else self.data.pop()
#
#     def peek(self):
#         return None if self.is_empty(self) else self.data[len(self.data) - 1]
#
#     def print(self):
#         print(self.data)


class Queue:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def add(self, record):
        self.stack_one.append(record)

    def remove(self):
        if len(self.stack_one) == 0:
            return None
        else:
            for i in range(0, len(self.stack_one)):
                self.stack_two.append(self.stack_one.pop())

            removed_record = self.stack_two.pop()

            for i in range(0, len(self.stack_two)):
                self.stack_one.append(self.stack_two.pop())

            return removed_record

    def peek(self):
        if len(self.stack_one) == 0:
            return None
        else:
            for i in range(0, len(self.stack_one)):
                self.stack_two.append(self.stack_one.pop())

            peek_record = self.stack_two.pop()
            self.stack_two.append(peek_record)

            for i in range(0, len(self.stack_two)):
                self.stack_one.append(self.stack_two.pop())

            return peek_record


class QfromSTest(unittest.TestCase):
    def test_add(self):
        try:
            queue = Queue()
            queue.add(1)
        except Exception:
            self.fail("raised exception", Exception)

    def test_remove(self):
        try:
            queue = Queue()
            queue.add(1)
            queue.remove()
        except Exception:
            self.fail("raised exception", Exception)

    def test_order_of_elements(self):
        q = Queue()
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(1, q.remove())
        self.assertEqual(2, q.remove())
        self.assertEqual(3, q.remove())
        self.assertEqual(None, q.remove())

    def test_peek(self):
        q = Queue()
        q.add(1)
        q.add(2)
        self.assertEqual(1, q.peek())
        self.assertEqual(1, q.peek())
        self.assertEqual(1, q.remove())
        self.assertEqual(2, q.remove())
