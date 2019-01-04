import math
import unittest


def first_solution(string):
    if type(string) is str:
        return string == string[::-1]
    else:
        return False


def second_solution(string):
    if type(string) is str:
        return string.find(string[::-1]) == 0
    else:
        return False


def third_solution(string):
    if type(string) is str:
        length_of_string = len(string)
        for i in range(0, math.floor(length_of_string / 2)):
            if string[i] != string[length_of_string - i - 1]:
                return False

        return True
    else:
        return False


class PalindromeTest(unittest.TestCase):
    def test_first_solution(self):
        self.assertTrue(first_solution("aba"))
        self.assertFalse(first_solution(" aba"))
        self.assertFalse(first_solution("aba "))
        self.assertFalse(first_solution("greetings"))
        self.assertTrue(first_solution("1000000001"))
        self.assertFalse(first_solution("Fish hsif"))
        self.assertTrue(first_solution("pennep"))
        self.assertTrue(first_solution(""))
        self.assertTrue(first_solution("a"))
        self.assertFalse(first_solution("twelve twins twirled twelve twigs"))
        self.assertFalse(first_solution(12))
        self.assertTrue(first_solution("step on no pets"))

    def test_second_solution(self):
        self.assertTrue(second_solution("aba"))
        self.assertFalse(second_solution(" aba"))
        self.assertFalse(second_solution("aba "))
        self.assertFalse(second_solution("greetings"))
        self.assertTrue(second_solution("1000000001"))
        self.assertFalse(second_solution("Fish hsif"))
        self.assertTrue(second_solution("pennep"))
        self.assertTrue(second_solution(""))
        self.assertTrue(second_solution("a"))
        self.assertFalse(second_solution("twelve twins twirled twelve twigs"))
        self.assertFalse(second_solution(12))
        self.assertTrue(second_solution("step on no pets"))

    def test_third_solution_solution(self):
        self.assertTrue(third_solution("aba"))
        self.assertFalse(third_solution(" aba"))
        self.assertFalse(third_solution("aba "))
        self.assertFalse(third_solution("greetings"))
        self.assertTrue(third_solution("1000000001"))
        self.assertFalse(third_solution("Fish hsif"))
        self.assertTrue(third_solution("pennep"))
        self.assertTrue(third_solution(""))
        self.assertTrue(third_solution("a"))
        self.assertFalse(third_solution("twelve twins twirled twelve twigs"))
        self.assertFalse(third_solution(12))
        self.assertTrue(third_solution("step on no pets"))
