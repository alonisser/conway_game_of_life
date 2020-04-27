import unittest
import numpy as np
from numpy.testing import assert_array_equal

from lib.generation import resolve_next_generation


class GenerationCreatorTestCase(unittest.TestCase):

    def test_all_dead_generation_resolves_to_all_dead_generation(self):
        original_generation = np.array([[0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])

        new_generation = resolve_next_generation(original_generation)
        assert_array_equal(original_generation, new_generation)


if __name__ == '__main__':
    unittest.main()
