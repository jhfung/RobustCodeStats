import numpy as np

def zeta(X, k=10, b=300, random_state=42):
    """Computes the partition cardinality of a matrix."""
    rng = np.random.default_rng(random_state)
    result = list()
    for _ in range(b):
        X_sample = rng.choice(X, axis=1, size=k, replace=True)
        z = len(np.unique(X_sample, axis=0)) / len(X_sample)
        result.append(z)
    return result

def eta(X, k=10, b=300, random_state=42):
    """Computes the partition entropy of a matrix."""
    rng = np.random.default_rng(random_state)
    result = list()
    for _ in range(b):
        X_sample = rng.choice(X, axis=1, size=k, replace=True)
        _, p = np.unique(X_sample, axis=0, return_counts=True)
        p = p / len(X_sample)
        h = -np.sum(p * np.log2(p)) / np.log2(len(X_sample))
        result.append(h)
    return result
