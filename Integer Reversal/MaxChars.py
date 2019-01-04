import unittest


def my_solution(string):
    char_frequency = {}
    for i in string:
        if i in char_frequency:
            char_frequency[i] = char_frequency[i] + 1
        else:
            char_frequency[i] = 1

    max_frequency = -1
    max_char = string[0]

    for i in char_frequency:
        if char_frequency[i] > max_frequency:
            max_frequency = char_frequency[i]
            max_char = i

    return max_char


class MaxCharsTest(unittest.TestCase):
    def test_my_solution(self):
        self.assertEqual(my_solution('a'), 'a')
        self.assertEqual(my_solution('abcdefghijklmnaaaaa'), 'a')
        self.assertEqual(my_solution('ab1c1d1e1f1g1'), '1')
