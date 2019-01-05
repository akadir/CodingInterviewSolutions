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
        self.assertEqual("dcba", first_solution("abcd"), )
        self.assertEqual("dcba ", first_solution(" abcd"), )
        self.assertEqual("", first_solution(""), )
        self.assertEqual("", first_solution(""), )
        self.assertEqual("a", first_solution("a"), )
        self.assertEqual("sgiwt evlewt delriwt sniwt evlewt", first_solution("twelve twins twirled twelve twigs"), )
        self.assertEqual(12, first_solution(12), )
        self.assertEqual("4321", first_solution("1234"), )

    def test_second_solution(self):
        self.assertEqual("dcba", second_solution("abcd"), )
        self.assertEqual("dcba ", second_solution(" abcd"), )
        self.assertEqual("", second_solution(""), )
        self.assertEqual("a", second_solution("a"), )
        self.assertEqual("sgiwt evlewt delriwt sniwt evlewt", second_solution("twelve twins twirled twelve twigs"), )
        self.assertEqual(12, second_solution(12), )
        self.assertEqual("4321", second_solution("1234"), )

    def test_third_solution(self):
        self.assertEqual("dcba", third_solution("abcd"), )
        self.assertEqual("dcba ", third_solution(" abcd"), )
        self.assertEqual("", third_solution(""), )
        self.assertEqual("a", third_solution("a"), )
        self.assertEqual("sgiwt evlewt delriwt sniwt evlewt", third_solution("twelve twins twirled twelve twigs"), )
        self.assertEqual(12, third_solution(12), )
        self.assertEqual("4321", third_solution("1234"), )
