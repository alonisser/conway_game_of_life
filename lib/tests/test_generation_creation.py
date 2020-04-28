import unittest
import numpy as np
from numpy.testing import assert_array_equal

from lib.generation import resolve_next_generation, generate_random_generation


class GenerationCreatorTestCase(unittest.TestCase):

    def test_all_dead_generation_resolves_to_all_dead_generation(self):
        original_generation = np.array([[0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])

        new_generation = resolve_next_generation(original_generation)
        assert_array_equal(original_generation, new_generation)

    def test_one_live_cell_generation_resolves_to_all_dead_generation(self):
        original_generation = np.array([[0, 0, 0, 0],
                                        [0, 1, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])

        new_generation = resolve_next_generation(original_generation)

        expected_generation = np.array([[0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])

        assert_array_equal(expected_generation, new_generation)

    def test_3_neighbour_cell_in_diagonal_keep_inner_cell_only_alive(self):
        original_generation = np.array([[0, 1, 0, 0, 0],
                                        [0, 0, 1, 0, 0],
                                        [0, 0, 0, 1, 0],
                                        [0, 0, 0, 0, 0]])

        new_generation = resolve_next_generation(original_generation)

        expected_generation = np.array([[0, 0, 0, 0, 0],
                                        [0, 0, 1, 0, 0],
                                        [0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0]])

        assert_array_equal(expected_generation, new_generation)

    def test_3_neighbour_cell_in_row_keep_inner_cell_only_alive_and_create_new_lives(self):
        original_generation = np.array([[0, 0, 0, 0, 0],
                                        [0, 1, 1, 1, 0],
                                        [0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0]])

        new_generation = resolve_next_generation(original_generation)

        expected_generation = np.array([[0, 0, 1, 0, 0],
                                        [0, 0, 1, 0, 0],
                                        [0, 0, 1, 0, 0],
                                        [0, 0, 0, 0, 0]])

        assert_array_equal(expected_generation, new_generation)

    def test_random_generation_creation_according_to_requested(self):
        x_size = 5
        y_size = 5
        live_cells = 3
        result = generate_random_generation(x_size=x_size, y_size=y_size, number_of_live_cells=live_cells)
        self.assertEqual(result.shape, (x_size, y_size))
        self.assertEqual(live_cells, result.sum())


if __name__ == '__main__':
    unittest.main()
