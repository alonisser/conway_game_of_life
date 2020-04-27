import unittest
import numpy as np

from lib.scorer import calculate_score


class ScorerTestCase(unittest.TestCase):
    def test_score_on_all_dead_matrix_is_zero(self):
        matrix = np.array([[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]])
        score = calculate_score(matrix, 0)
        self.assertEqual(score, 0)

    def test_score_on_central_live_and_rest_dead_is_zero(self):
        matrix = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]])
        score = calculate_score(matrix, 1)
        self.assertEqual(score, 0)

    def test_score_for_3_neighbours_and_dead_cell_is_one(self):
        matrix = np.array([[1, 1, 0],
                           [0, 0, 1],
                           [0, 0, 0]])
        score = calculate_score(matrix, 0)
        self.assertEqual(score, 1)

    def test_score_for_3_neighbours_and_live_cell_is_one(self):
        matrix = np.array([[1, 1, 0],
                           [0, 1, 1],
                           [0, 0, 0]])
        score = calculate_score(matrix, 1)
        self.assertEqual(score, 1)

    def test_score_for_5_neighbours_and_live_cell_is_zero(self):
        matrix = np.array([[1, 1, 1],
                           [1, 1, 1],
                           [0, 0, 0]])
        score = calculate_score(matrix, 1)
        self.assertEqual(score, 0)

    def test_score_for_4_neighbours_and_dead_cell_is_zero(self):
        matrix = np.array([[1, 1, 1],
                           [0, 0, 1],
                           [0, 0, 0]])
        score = calculate_score(matrix, 0)
        self.assertEqual(score, 0)

    def test_score_for_3_neighbours_and_dead_cell_is_one(self):
        matrix = np.array([[1, 1, 0],
                           [0, 0, 1],
                           [0, 0, 0]])
        score = calculate_score(matrix, 0)
        self.assertEqual(score, 1)

    def test_score_for_2_neighbours_and_dead_cell_is_zero(self):
        matrix = np.array([[1, 1, 0],
                           [0, 0, 0],
                           [0, 0, 0]])
        score = calculate_score(matrix, 0)
        self.assertEqual(score, 0)

if __name__ == '__main__':
    unittest.main()
