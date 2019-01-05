import unittest


def fizz_buzz(number):
    if number % 15 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return number


class FizzBuzzTest(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(1, fizz_buzz(1))
        self.assertEqual(2, fizz_buzz(2))
        self.assertEqual('fizz', fizz_buzz(3))
        self.assertEqual(4, fizz_buzz(4))
        self.assertEqual('buzz', fizz_buzz(5))
        self.assertEqual('fizz', fizz_buzz(6))
        self.assertEqual(7, fizz_buzz(7))
        self.assertEqual('fizz', fizz_buzz(9))
        self.assertEqual('buzz', fizz_buzz(10))
        self.assertEqual('fizzbuzz', fizz_buzz(15))
