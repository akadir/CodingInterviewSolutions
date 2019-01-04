import math
import unittest


# first solution that comes to my mind
def my_solution(string):
    if type(string) is str:
        return string == string[::-1]
    else:
        return False


def alternate_solution(string):
    if type(string) is str:
        return string.find(string[::-1]) == 0
    else:
        return False


def loop_through_solution(string):
    if type(string) is str:
        length_of_string = len(string)
        for i in range(0, math.floor(length_of_string / 2)):
            if string[i] != string[length_of_string - i - 1]:
                return False

        return True
    else:
        return False


class StringReversalTest(unittest.TestCase):
    def test_my_solution(self):
        self.assertTrue(my_solution("aba"))
        self.assertFalse(my_solution(" aba"))
        self.assertFalse(my_solution("aba "))
        self.assertFalse(my_solution("greetings"))
        self.assertTrue(my_solution("1000000001"))
        self.assertFalse(my_solution("Fish hsif"))
        self.assertTrue(my_solution("pennep"))
        self.assertTrue(my_solution(""))
        self.assertTrue(my_solution("a"))
        self.assertFalse(my_solution("twelve twins twirled twelve twigs"))
        self.assertFalse(my_solution(12))
        self.assertTrue(my_solution("step on no pets"))

    def test_alternate_solution(self):
        self.assertTrue(alternate_solution("aba"))
        self.assertFalse(alternate_solution(" aba"))
        self.assertFalse(alternate_solution("aba "))
        self.assertFalse(alternate_solution("greetings"))
        self.assertTrue(alternate_solution("1000000001"))
        self.assertFalse(alternate_solution("Fish hsif"))
        self.assertTrue(alternate_solution("pennep"))
        self.assertTrue(alternate_solution(""))
        self.assertTrue(alternate_solution("a"))
        self.assertFalse(alternate_solution("twelve twins twirled twelve twigs"))
        self.assertFalse(alternate_solution(12))
        self.assertTrue(alternate_solution("step on no pets"))

    def test_loop_through_solution(self):
        self.assertTrue(loop_through_solution("aba"))
        self.assertFalse(loop_through_solution(" aba"))
        self.assertFalse(loop_through_solution("aba "))
        self.assertFalse(loop_through_solution("greetings"))
        self.assertTrue(loop_through_solution("1000000001"))
        self.assertFalse(loop_through_solution("Fish hsif"))
        self.assertTrue(loop_through_solution("pennep"))
        self.assertTrue(loop_through_solution(""))
        self.assertTrue(loop_through_solution("a"))
        self.assertFalse(loop_through_solution("twelve twins twirled twelve twigs"))
        self.assertFalse(loop_through_solution(12))
        self.assertTrue(loop_through_solution("step on no pets"))
