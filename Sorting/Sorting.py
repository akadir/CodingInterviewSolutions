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
