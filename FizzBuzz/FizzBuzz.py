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
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(3), 'fizz')
        self.assertEqual(fizz_buzz(4), 4)
        self.assertEqual(fizz_buzz(5), 'buzz')
        self.assertEqual(fizz_buzz(6), 'fizz')
        self.assertEqual(fizz_buzz(7), 7)
        self.assertEqual(fizz_buzz(9), 'fizz')
        self.assertEqual(fizz_buzz(10), 'buzz')
        self.assertEqual(fizz_buzz(15), 'fizzbuzz')
