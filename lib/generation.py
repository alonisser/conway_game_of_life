import numpy as np


def resolve_next_generation(generation: np.ndarray) -> np.ndarray:
    return np.zeros(generation.size).reshape(generation.shape)


def get_neighbours(address):
    pass
