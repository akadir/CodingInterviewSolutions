import unittest


def first_solution(sentence):
    return ' '.join(word[0].upper() + word[1:] for word in sentence.split())


def second_solution(sentence):
    return sentence.title()


def third_solution(sentence):
    words = []
    for word in sentence.split(' '):
        words.append(word[0].capitalize() + word[1:])

    return ' '.join(words)


def fourth_solution(sentence):
    result = sentence[0].capitalize()
    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            result += sentence[i].capitalize()
        else:
            result += sentence[i]
    return result


class TestCapitalize(unittest.TestCase):
    def test_first_solution(self):
        self.assertEqual(first_solution('hi there, how is it going?'), 'Hi There, How Is It Going?')
        self.assertEqual(first_solution('i love breakfast at bill miller bbq'), 'I Love Breakfast At Bill Miller Bbq')

    def test_second_solution(self):
        self.assertEqual(second_solution('hi there, how is it going?'), 'Hi There, How Is It Going?')
        self.assertEqual(second_solution('i love breakfast at bill miller bbq'), 'I Love Breakfast At Bill Miller Bbq')

    def test_third_solution(self):
        self.assertEqual(third_solution('hi there, how is it going?'), 'Hi There, How Is It Going?')
        self.assertEqual(third_solution('i love breakfast at bill miller bbq'), 'I Love Breakfast At Bill Miller Bbq')

    def test_fourth_solution(self):
        self.assertEqual(fourth_solution('hi there, how is it going?'), 'Hi There, How Is It Going?')
        self.assertEqual(fourth_solution('i love breakfast at bill miller bbq'), 'I Love Breakfast At Bill Miller Bbq')
