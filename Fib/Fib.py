import unittest


def iterative_solution(number):
    result = [0, 1]

    for i in range(2, number + 1):
        a = result[i - 1]
        b = result[i - 2]

        result.append(a + b)

    return result[number]


def recursive_solution(number):
    if number < 2:
        return number

    return recursive_solution(number - 1) + recursive_solution(number - 2)


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def recursive_solution_with_memoization(number):
    if number < 2:
        return number

    return recursive_solution_with_memoization(number - 1) + recursive_solution_with_memoization(number - 2)


class FibTest(unittest.TestCase):
    def test_iterative_solution(self):
        self.assertEqual(1, iterative_solution(1))
        self.assertEqual(1, iterative_solution(2))
        self.assertEqual(2, iterative_solution(3))
        self.assertEqual(3, iterative_solution(4))
        self.assertEqual(610, iterative_solution(15))

    def test_recursive_solution(self):
        self.assertEqual(1, recursive_solution(1))
        self.assertEqual(1, recursive_solution(2))
        self.assertEqual(2, recursive_solution(3))
        self.assertEqual(3, recursive_solution(4))
        self.assertEqual(610, recursive_solution(15))

    def test_recursive_solution_with_memoization(self):
        self.assertEqual(1, recursive_solution_with_memoization(1))
        self.assertEqual(1, recursive_solution_with_memoization(2))
        self.assertEqual(2, recursive_solution_with_memoization(3))
        self.assertEqual(3, recursive_solution_with_memoization(4))
        self.assertEqual(610, recursive_solution_with_memoization(15))
        self.assertEqual(63245986, recursive_solution_with_memoization(39))
