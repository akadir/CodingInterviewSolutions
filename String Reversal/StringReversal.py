import unittest


# first solution that comes to my mind
def my_solution(string_to_be_reversed):
    if type(string_to_be_reversed) is str:
        reversed_string = ""

        for x in string_to_be_reversed[::-1]:
            reversed_string += x

        return reversed_string
    else:
        return string_to_be_reversed


# better solution
def built_in_solution(string_to_be_reversed):
    if type(string_to_be_reversed) is str:
        return string_to_be_reversed[::-1]
    else:
        return string_to_be_reversed


# another loop through solution
def another_solution(string_to_be_reversed):
    if type(string_to_be_reversed) is str:
        reversed_string = ""

        for x in string_to_be_reversed:
            reversed_string = x + reversed_string

        return reversed_string
    else:
        return string_to_be_reversed


class StringReversalTest(unittest.TestCase):
    def test_my_solution(self):
        self.assertEqual(my_solution(""), "")
        self.assertEqual(my_solution("a"), "a")
        self.assertEqual(my_solution("twelve twins twirled twelve twigs"), "sgiwt evlewt delriwt sniwt evlewt")
        self.assertEqual(my_solution(12), 12)
        self.assertEqual(my_solution("1234"), "4321")

    def test_built_in_solution(self):
        self.assertEqual(built_in_solution(""), "")
        self.assertEqual(built_in_solution("a"), "a")
        self.assertEqual(built_in_solution("twelve twins twirled twelve twigs"), "sgiwt evlewt delriwt sniwt evlewt")
        self.assertEqual(built_in_solution(12), 12)
        self.assertEqual(built_in_solution("1234"), "4321")

    def test_loop_through_solution(self):
        self.assertEqual(another_solution(""), "")
        self.assertEqual(another_solution("a"), "a")
        self.assertEqual(another_solution("twelve twins twirled twelve twigs"), "sgiwt evlewt delriwt sniwt evlewt")
        self.assertEqual(another_solution(12), 12)
        self.assertEqual(another_solution("1234"), "4321")
