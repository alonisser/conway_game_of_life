import unittest
import numpy as np
from numpy.testing import assert_array_equal

from lib.generation import get_neighbours


class NeighboursTestCase(unittest.TestCase):
    def test_neighbours_for_central_position(self):
        generation = np.array([[0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0]])
        sub_matrix = get_neighbours((1, 2), generation)
        expected_matrix = np.array([[0, 0, 0],
                                    [1, 1, 1],
                                    [0, 0, 0]])
        assert_array_equal(sub_matrix, expected_matrix)


if __name__ == '__main__':
    unittest.main()
