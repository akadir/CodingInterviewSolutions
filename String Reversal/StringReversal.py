import unittest


def first_solution(string_to_be_reversed):
    if type(string_to_be_reversed) is str:
        reversed_string = ""

        for x in string_to_be_reversed[::-1]:
            reversed_string += x

        return reversed_string
    else:
        return string_to_be_reversed


def second_solution(string_to_be_reversed):
    if type(string_to_be_reversed) is str:
        return string_to_be_reversed[::-1]
    else:
        return string_to_be_reversed


def third_solution(string_to_be_reversed):
    if type(string_to_be_reversed) is str:
        reversed_string = ""

        for x in string_to_be_reversed:
            reversed_string = x + reversed_string

        return reversed_string
    else:
        return string_to_be_reversed


class StringReversalTest(unittest.TestCase):
    def test_first_solution(self):
        self.assertEqual(first_solution("abcd"), "dcba")
        self.assertEqual(first_solution(" abcd"), "dcba ")
        self.assertEqual(first_solution(""), "")
        self.assertEqual(first_solution(""), "")
        self.assertEqual(first_solution("a"), "a")
        self.assertEqual(first_solution("twelve twins twirled twelve twigs"), "sgiwt evlewt delriwt sniwt evlewt")
        self.assertEqual(first_solution(12), 12)
        self.assertEqual(first_solution("1234"), "4321")

    def test_second_solution(self):
        self.assertEqual(second_solution("abcd"), "dcba")
        self.assertEqual(second_solution(" abcd"), "dcba ")
        self.assertEqual(second_solution(""), "")
        self.assertEqual(second_solution("a"), "a")
        self.assertEqual(second_solution("twelve twins twirled twelve twigs"), "sgiwt evlewt delriwt sniwt evlewt")
        self.assertEqual(second_solution(12), 12)
        self.assertEqual(second_solution("1234"), "4321")

    def test_third_solution(self):
        self.assertEqual(third_solution("abcd"), "dcba")
        self.assertEqual(third_solution(" abcd"), "dcba ")
        self.assertEqual(third_solution(""), "")
        self.assertEqual(third_solution("a"), "a")
        self.assertEqual(third_solution("twelve twins twirled twelve twigs"), "sgiwt evlewt delriwt sniwt evlewt")
        self.assertEqual(third_solution(12), 12)
        self.assertEqual(third_solution("1234"), "4321")
