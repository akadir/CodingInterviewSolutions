import math
import unittest


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                lesser = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = lesser
    return arr


def selection_sort(arr):
    for i in range(0, len(arr)):
        index_of_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index_of_min]:
                index_of_min = j
        if index_of_min is not i:
            lesser = arr[index_of_min]
            arr[index_of_min] = arr[i]
            arr[i] = lesser
    return arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    center = math.floor(len(arr) / 2)
    left = arr[0:center]
    right = arr[center:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    results = []

    while len(left) > 0 and len(right):
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))

    return results + left + right


class SortingTest(unittest.TestCase):
    @staticmethod
    def get_array():
        return [100, -40, 500, -124, 0, 21, 7]

    @staticmethod
    def get_sorted_array():
        return [-124, -40, 0, 7, 21, 100, 500]

    def test_bubble_sort(self):
        self.assertEqual(self.get_sorted_array(), bubble_sort(self.get_array()))

    def test_selection_sort(self):
        self.assertEqual(self.get_sorted_array(), selection_sort(self.get_array()))

    def test_merge(self):
        left = [1, 10]
        right = [2, 8, 12]

        self.assertEqual([1, 2, 8, 10, 12], merge(left, right))

    def test_merge_sort(self):
        self.assertEqual(self.get_sorted_array(), merge_sort(self.get_array()))
