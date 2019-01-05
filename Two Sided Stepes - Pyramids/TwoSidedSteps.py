import math
import sys
import unittest
from io import StringIO


def first_solution(number):
    max_col = number * 2 - 1
    for row in range(0, number):
        row_sharp_count = (row + 1) * 2 - 1
        for col in range(0, max_col):
            if col < (max_col - row_sharp_count) // 2:
                print(' ', end='')
            elif col >= ((max_col - row_sharp_count) // 2) + row_sharp_count:
                print(' ', end='')
            else:
                print('#', end='')
        print('')


def second_solution(number):
    midpoint = math.floor((2 * number - 1) / 2)

    for row in range(0, number):
        level = ''

        for column in range(0, 2 * number - 1):
            if midpoint - row <= column <= midpoint + row:
                level += '#'
            else:
                level += ' '

        print(level)


def third_solution(number, row=0, level=''):
    if row == number:
        return

    if len(level) == (2 * number - 1):
        print(level)
        return third_solution(number, row + 1)

    midpoint = math.floor((2 * number - 1) / 2)

    if midpoint - row <= len(level) <= midpoint + row:
        level += '#'
    else:
        level += ' '

    third_solution(number, row, level)


class TwoSidedStepsTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_call_first_solution_with_two(self):
        first_solution(2)
        self.assertEqual(sys.stdout.getvalue(), ' # \n###\n')

    def test_call_first_solution_with_three(self):
        first_solution(3)
        self.assertEqual(sys.stdout.getvalue(), '  #  \n ### \n#####\n')

    def test_call_first_solution_with_four(self):
        first_solution(4)
        self.assertEqual(sys.stdout.getvalue(), '   #   \n  ###  \n ##### \n#######\n')

    def test_call_second_solution_with_two(self):
        second_solution(2)
        self.assertEqual(sys.stdout.getvalue(), ' # \n###\n')

    def test_call_second_solution_with_three(self):
        second_solution(3)
        self.assertEqual(sys.stdout.getvalue(), '  #  \n ### \n#####\n')

    def test_call_second_solution_with_four(self):
        second_solution(4)
        self.assertEqual(sys.stdout.getvalue(), '   #   \n  ###  \n ##### \n#######\n')

    def test_call_third_solution_with_two(self):
        third_solution(2)
        self.assertEqual(sys.stdout.getvalue(), ' # \n###\n')

    def test_call_third_solution_with_three(self):
        third_solution(3)
        self.assertEqual(sys.stdout.getvalue(), '  #  \n ### \n#####\n')

    def test_call_third_solution_with_four(self):
        third_solution(4)
        self.assertEqual(sys.stdout.getvalue(), '   #   \n  ###  \n ##### \n#######\n')
