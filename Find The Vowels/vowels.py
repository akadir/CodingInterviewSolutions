import re
import unittest


def first_solution(text):
    text = re.sub('[^(aeiou)]', '', text.lower())
    return len(text)


def second_solution(text):
    count = 0
    checker = 'aeiou'
    for i in text:
        if i.lower() in checker:
            count += 1

    return count


class VowelsTest(unittest.TestCase):
    def test_first_solution(self):
        self.assertEqual(5, first_solution('aeiou'))
        self.assertEqual(5, first_solution('abcdefghijklmnopqrstuvwxyz'))
        self.assertEqual(0, first_solution('bcdfghjkl'))

    def test_second_solution(self):
        self.assertEqual(5, second_solution('aeiou'))
        self.assertEqual(5, second_solution('abcdefghijklmnopqrstuvwxyz'))
        self.assertEqual(0, second_solution('bcdfghjkl'))
