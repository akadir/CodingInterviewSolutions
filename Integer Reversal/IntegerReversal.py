import unittest


def first_solution(integer_to_be_reversed):
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


def second_solution(integer_to_be_reversed):
    string = str(integer_to_be_reversed)
    reversed_string = string[::-1].replace('-', '')
    reversed_int = int(reversed_string)
    if integer_to_be_reversed < 0:
        reversed_int *= -1

    return reversed_int


class IntegerReversalTest(unittest.TestCase):
    def test_first_solution(self):
        self.assertEqual(0, first_solution(0))
        self.assertEqual(5, first_solution(5))
        self.assertEqual(51, first_solution(15))
        self.assertEqual(9, first_solution(90))
        self.assertEqual(9532, first_solution(2359))
        self.assertEqual(-5, first_solution(-5))
        self.assertEqual(-51, first_solution(-15))
        self.assertEqual(-9, first_solution(-90))
        self.assertEqual(-9532, first_solution(-2359))

    def test_second_solution(self):
        self.assertEqual(0, second_solution(0))
        self.assertEqual(5, second_solution(5))
        self.assertEqual(51, second_solution(15))
        self.assertEqual(9, second_solution(90))
        self.assertEqual(9532, second_solution(2359))
        self.assertEqual(-5, second_solution(-5))
        self.assertEqual(-51, second_solution(-15))
        self.assertEqual(-9, second_solution(-90))
        self.assertEqual(-9532, second_solution(-2359))
