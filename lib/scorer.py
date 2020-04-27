from numpy import int64
import numpy as np


def calculate_score(sub_matrix: np.ndarray, central_value: int64):
    res = sub_matrix.sum() - central_value
    if res == 3:
        return 1
    elif res >= 4:
        return 0
    elif res < 2:
        return 0

    return central_value
