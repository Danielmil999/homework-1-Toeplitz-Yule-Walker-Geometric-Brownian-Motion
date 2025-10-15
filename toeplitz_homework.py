import numpy as np
from scipy.linalg import toeplitz
import timeit

# ----------------------
# 1. Toeplitz Matrix (manual)
# ----------------------

def toeplitz_matrix(dim, seq, verbose=True):
    if not isinstance(dim, int):
        if verbose: print("❌ Error: 'dim' must be an integer.")
        return None
    if dim <= 0:
        if verbose: print("❌ Error: 'dim' must be positive.")
        return None
    if not all(isinstance(x, (int, float)) for x in seq):
        if verbose: print("❌ Error: 'seq' must contain only numbers.")
        return None
    if dim > len(seq):
        if verbose: print(f"❌ Error: 'dim' cannot exceed length of 'seq' ({len(seq)}).")
        return None

    T = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            T[i, j] = seq[dim - 1 + i - j]
    return T


# Example comparison
dim = 4
seq = list(range(1, 8))
custom_T = toeplitz_matrix(dim, seq)
scipy_T = toeplitz(range(4, 8), range(4, 0, -1))
print("Custom Toeplitz:\n", custom_T)
print("SciPy Toeplitz:\n", scipy_T)

# ----------------------
# 2. Timing comparison
# ----------------------

def scipy_toeplitz():
    return toeplitz(seq)

def custom_toeplitz():
    return toeplitz_matrix(dim, seq, verbose=False)

t1 = timeit.timeit(custom_toeplitz, number=1000)
t2 = timeit.timeit(scipy_toeplitz, number=1000)
print(f"Custom function time: {t1:.5f}s")
print(f"SciPy function time:  {t2:.5f}s")
