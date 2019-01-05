import sys
import unittest
from io import StringIO


def first_solution(number):
    if number < 0:
        return
    else:
        for i in range(1, number + 1):
            for j in range(0, number):
                if j < i:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()


def second_solution(number):
    for row in range(0, number):
        stair = ''
        for column in range(0, number):
            if column <= row:
                stair += '#'
            else:
                stair += ' '
        print(stair)


def third_solution(number, row=0, stair=''):
    if number == row:
        return

    if number == len(stair):
        print(stair)
        return third_solution(number, row + 1)

    if len(stair) <= row:
        stair += '#'
    else:
        stair += ' '

    third_solution(number, row, stair)


class StepsTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_call_first_solution_with_one(self):
        first_solution(1)
        self.assertEqual('#\n', sys.stdout.getvalue())

    def test_call_first_solution_with_two(self):
        first_solution(2)
        self.assertEqual('# \n##\n', sys.stdout.getvalue())

    def test_call_first_solution_with_three(self):
        first_solution(3)
        self.assertEqual('#  \n## \n###\n', sys.stdout.getvalue())

    def test_call_second_solution_with_one(self):
        second_solution(1)
        self.assertEqual('#\n', sys.stdout.getvalue())

    def test_call_second_solution_with_two(self):
        second_solution(2)
        self.assertEqual('# \n##\n', sys.stdout.getvalue())

    def test_call_second_solution_with_three(self):
        second_solution(3)
        self.assertEqual('#  \n## \n###\n', sys.stdout.getvalue())

    def test_call_third_solution_with_one(self):
        third_solution(1)
        self.assertEqual('#\n', sys.stdout.getvalue())

    def test_call_third_solution_with_two(self):
        third_solution(2)
        self.assertEqual('# \n##\n', sys.stdout.getvalue())

    def test_call_third_solution_with_three(self):
        third_solution(3)
        self.assertEqual('#  \n## \n###\n', sys.stdout.getvalue())