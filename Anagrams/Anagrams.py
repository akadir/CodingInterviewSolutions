import re
import unittest


def get_alpha_numeric_character_counts(word):
    word = re.sub('[^\w]g', '', word)
    word.lower()
    char_frequency = {}
    for i in word:
        if i in char_frequency:
            char_frequency[i] = char_frequency[i] + 1
        else:
            char_frequency[i] = 1

    return char_frequency


def first_solution(word_one, word_two):
    word_one_frequency = get_alpha_numeric_character_counts(word_one)
    word_two_frequency = get_alpha_numeric_character_counts(word_two)

    if len(word_one_frequency) != len(word_two_frequency):
        return False
    else:
        for key in word_one_frequency:
            if word_one_frequency[key] != word_two_frequency[key]:
                return False

    return True


def second_solution(word_one, word_two):
    word_one = re.sub('[^\w]g', '', word_one).lower()
    word_two = re.sub('[^\w]g', '', word_two).lower()
    word_one = list(word_one)
    word_one.sort()
    word_two = list(word_two)
    word_two.sort()

    return word_two == word_one


class AnagramsTest(unittest.TestCase):
    def test_first_solution(self):
        self.assertTrue(first_solution('hello', 'llohe'))
        self.assertTrue(first_solution('Whoa! Hi!', 'Hi! Whoa!'))
        self.assertFalse(first_solution('One One', 'Two two two'))
        self.assertFalse(first_solution('One one', 'One one c'))
        self.assertFalse(first_solution('A tree, a life, a bench', 'A tree, a fence, a yard'))

    def test_second_solution(self):
        self.assertTrue(second_solution('hello', 'llohe'))
        self.assertTrue(second_solution('Whoa! Hi!', 'Hi! Whoa!'))
        self.assertFalse(second_solution('One One', 'Two two two'))
        self.assertFalse(second_solution('One one', 'One one c'))
        self.assertFalse(second_solution('A tree, a life, a bench', 'A tree, a fence, a yard'))
