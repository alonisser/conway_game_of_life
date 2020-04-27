
import numpy as np

from lib.scorer import calculate_score


def resolve_next_generation(generation: np.ndarray) -> np.ndarray:
    # Naive implementation, not using vectorize, fromiter etc
    next_generation = np.empty(generation.shape)

    for addr, value in np.ndenumerate(generation):
        sub_matrix = get_neighbours(address=addr, matrix=generation)
        # Can you spot the bug?
        next_generation[addr] = calculate_score(sub_matrix, value)

    return next_generation


def get_neighbours(address, matrix: np.ndarray) -> np.ndarray :
    row = address[0]
    column = address[1]
    # Can you spot the bug?
    first_row = row - 1
    last_row = row + 1
    first_column = column -1
    last_column = column + 1
    sub_matrix = matrix[first_row: last_row, first_column: last_column]
    return sub_matrix
