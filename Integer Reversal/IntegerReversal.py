import unittest


def my_solution(integer_to_be_reversed):
    x = 0
    n = integer_to_be_reversed
    if integer_to_be_reversed < 0:
        n *= -1
    while n > 0:
        x *= 10
        x += n % 10
        n //= 10
    if integer_to_be_reversed < 0:
        return int("-" + repr(x))
    return x


def solve_by_using_string_reversal(integer_to_be_reversed):
    string = str(integer_to_be_reversed)
    reversed_string = string[::-1].replace('-', '')
    reversed_int = int(reversed_string)
    if integer_to_be_reversed < 0:
        reversed_int *= -1

    return reversed_int


class IntegerReversalTest(unittest.TestCase):
    def test_my_solution(self):
        self.assertEqual(my_solution(0), 0)
        self.assertEqual(my_solution(5), 5)
        self.assertEqual(my_solution(15), 51)
        self.assertEqual(my_solution(90), 9)
        self.assertEqual(my_solution(2359), 9532)
        self.assertEqual(my_solution(-5), -5)
        self.assertEqual(my_solution(-15), -51)
        self.assertEqual(my_solution(-90), -9)
        self.assertEqual(my_solution(-2359), -9532)

    def test_solve_by_using_string_reversal(self):
        self.assertEqual(solve_by_using_string_reversal(0), 0)
        self.assertEqual(solve_by_using_string_reversal(5), 5)
        self.assertEqual(solve_by_using_string_reversal(15), 51)
        self.assertEqual(solve_by_using_string_reversal(90), 9)
        self.assertEqual(solve_by_using_string_reversal(2359), 9532)
        self.assertEqual(solve_by_using_string_reversal(-5), -5)
        self.assertEqual(solve_by_using_string_reversal(-15), -51)
        self.assertEqual(solve_by_using_string_reversal(-90), -9)
        self.assertEqual(solve_by_using_string_reversal(-2359), -9532)
