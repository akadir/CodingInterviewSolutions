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
        self.assertEqual('Hi There, How Is It Going?', first_solution('hi there, how is it going?'))
        self.assertEqual('I Love Breakfast At Bill Miller Bbq', first_solution('i love breakfast at bill miller bbq'))

    def test_second_solution(self):
        self.assertEqual('Hi There, How Is It Going?', second_solution('hi there, how is it going?'))
        self.assertEqual('I Love Breakfast At Bill Miller Bbq', second_solution('i love breakfast at bill miller bbq'))

    def test_third_solution(self):
        self.assertEqual('Hi There, How Is It Going?', third_solution('hi there, how is it going?'))
        self.assertEqual('I Love Breakfast At Bill Miller Bbq', third_solution('i love breakfast at bill miller bbq'))

    def test_fourth_solution(self):
        self.assertEqual('Hi There, How Is It Going?', fourth_solution('hi there, how is it going?'))
        self.assertEqual('I Love Breakfast At Bill Miller Bbq', fourth_solution('i love breakfast at bill miller bbq'))
