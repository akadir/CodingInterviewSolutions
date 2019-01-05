import unittest


def first_solution(number):
    result = []

    for i in range(0, number):
        result.append([None] * number)

    counter = 1
    start_row = 0
    end_row = number - 1
    start_column = 0
    end_column = number - 1

    while start_column <= end_column and start_row <= end_row:
        i = start_column
        while start_column <= i <= end_column:
            result[start_row][i] = counter
            counter += 1
            i += 1

        start_row += 1

        i = start_row
        while start_row <= i <= end_row:
            result[i][end_column] = counter
            counter += 1
            i += 1

        end_column -= 1

        i = end_column
        while end_column >= i >= start_column:
            result[end_row][i] = counter
            counter += 1
            i -= 1

        end_row -= 1

        i = end_row
        while end_row >= i >= start_row:
            result[i][start_column] = counter
            counter += 1
            i -= 1

        start_column += 1

    return result


class MatrixSpiralTest(unittest.TestCase):
    def test_first_solution(self):
        m = first_solution(2)
        self.assertEqual(2, len(m))
        self.assertEqual([1, 2], m[0])
        self.assertEqual([4, 3], m[1])

        m = first_solution(3)
        self.assertEqual(3, len(m))
        self.assertEqual([1, 2, 3], m[0])
        self.assertEqual([8, 9, 4], m[1])
        self.assertEqual([7, 6, 5], m[2])

        m = first_solution(4)
        self.assertEqual(4, len(m))
        self.assertEqual([1, 2, 3, 4], m[0])
        self.assertEqual([12, 13, 14, 5], m[1])
        self.assertEqual([11, 16, 15, 6], m[2])
        self.assertEqual([10, 9, 8, 7], m[3])
