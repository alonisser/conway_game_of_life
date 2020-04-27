from numpy import int64
import numpy as np


def calculate_score(sub_matrix: np.ndarray, central_value: int64):
    res = sub_matrix.sum() - central_value
    if 1 < res < 4:
        return 1
    elif res >= 4:
        return 0

    return res
