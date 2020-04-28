import numpy as np

from scorer import calculate_score


def resolve_next_generation(generation: np.ndarray) -> np.ndarray:
    # Naive implementation, not using vectorize, fromiter etc
    next_generation = np.empty(generation.shape)

    for addr, value in np.ndenumerate(generation):
        sub_matrix = get_neighbours(address=addr, matrix=generation)
        # Can you spot the bug?
        score = calculate_score(sub_matrix, value)
        next_generation[addr[0], addr[1]] = score

    return next_generation


def get_neighbours(address, matrix: np.ndarray) -> np.ndarray:
    row = address[0]
    column = address[1]
    first_row = row - 1 if row > 0 else 0
    last_row = row + 2
    first_column = column - 1 if column > 0 else 0
    last_column = column + 2
    sub_matrix = matrix[first_row: last_row, first_column: last_column]
    return sub_matrix


def generate_random_generation(x_size: int, y_size: int, number_of_live_cells: int) -> np.ndarray:
    total_cells = x_size * y_size
    generation = np.array([1] * number_of_live_cells + [0] * (total_cells - number_of_live_cells)).reshape(
        (x_size, y_size))
    np.random.shuffle(generation)

    return generation
