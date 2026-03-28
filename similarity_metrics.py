import numpy as np

# Small constant to avoid division by zero
EPS = 1e-12


def l2_distance(x, y):
    """
    Euclidean distance (L2 norm)
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    return float(np.sqrt(np.sum((x - y) ** 2)))


def l1_distance(x, y):
    """
    Manhattan distance (L1 norm)
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    return float(np.sum(np.abs(x - y)))


def dot_product(x, y):
    """
    Dot product of two vectors
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    return float(np.sum(x * y))


def l2_norm(x):
    """
    L2 norm (vector magnitude)
    """
    x = np.array(x, dtype=float)
    return float(np.sqrt(np.sum(x ** 2)))


def cosine_similarity(x, y):
    """
    Cosine similarity between two vectors
    """
    return float(dot_product(x, y) / (l2_norm(x) * l2_norm(y) + EPS))
