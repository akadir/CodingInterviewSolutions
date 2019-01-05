import math
import unittest


def first_solution(array, size):
    chunked = []
    for i in range(0, math.ceil(len(array) / size)):
        tmpArr = []
        for j in range(0, size):
            if (i * size + j) < len(array):
                tmpArr.append(array[i * size + j])
        chunked.append(tmpArr)
    return chunked


def second_solution(array, size):
    chunked = []

    for i in array:
        last = len(chunked) - 1
        if last < 0 or len(chunked[last]) == size:
            chunked.append([i])
        else:
            chunked[last].append(i)

    return chunked


def third_solution(array, size):
    chunked = []
    index = 0

    while index < len(array):
        chunked.append(array[index:size + index])
        index += size

    return chunked


class TestArrayChunking(unittest.TestCase):
    def test_first_solution(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], first_solution(arr, 2))
        arr = [1, 2, 3]
        self.assertEqual([[1], [2], [3]], first_solution(arr, 1))
        arr = [1, 2, 3, 4, 5]
        self.assertEqual([[1, 2, 3], [4, 5]], first_solution(arr, 3))
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]], first_solution(arr, 5))

    def test_second_solution(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], second_solution(arr, 2))
        arr = [1, 2, 3]
        self.assertEqual([[1], [2], [3]], second_solution(arr, 1))
        arr = [1, 2, 3, 4, 5]
        self.assertEqual([[1, 2, 3], [4, 5]], second_solution(arr, 3))
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]], second_solution(arr, 5))

    def test_third_solution(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], third_solution(arr, 2))
        arr = [1, 2, 3]
        self.assertEqual([[1], [2], [3]], third_solution(arr, 1))
        arr = [1, 2, 3, 4, 5]
        self.assertEqual([[1, 2, 3], [4, 5]], third_solution(arr, 3))
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]], third_solution(arr, 5))
