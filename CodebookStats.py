import numpy as np

def zeta(X, k=10, b=300, random_state=42):
    """Computes the partition cardinality of a matrix.
    
    Parameters
    ----------
    X : ndarray
        The input binary matrix.

    k : int, optional, default=10
        The size of each subsampled feature subset.

    b : int, optional, default=300
        The number of subsamples to generate.

    random_state : int or RandomState, optional, default=42
        The seed for the random number generator.  Provides reproducibility of results.

    Returns
    -------
    result : list of float
        A list containing the partition cardinality values for each of the `b` bootstrap samples.  Each value is the proportion of unique rows in the input matrix using only the `k` subsampled features.  
    """

    rng = np.random.default_rng(random_state)
    result = list()
    for _ in range(b):
        X_sample = rng.choice(X, axis=1, size=k, replace=True)
        z = len(np.unique(X_sample, axis=0)) / len(X_sample)
        result.append(z)
    return result

def eta(X, k=10, b=300, random_state=42):
    """Computes the partition entropy of a matrix.
    
    Parameters
    ----------
    X : ndarray
        The input binary matrix.

    k : int, optional, default=10
        The size of each subsampled feature subset.

    b : int, optional, default=300
        The number of subsamples to generate.

    random_state : int or RandomState, optional, default=42
        The seed for the random number generator.  Provides reproducibility of results.

    Returns
    -------
    result : list of float
        A list containing the partition entropy values for each of the `b` bootstrap samples.  Each value is the normalized entropy the distribution of unique rows in the input matrix using only the `k` subsampled features.
    """

    rng = np.random.default_rng(random_state)
    result = list()
    for _ in range(b):
        X_sample = rng.choice(X, axis=1, size=k, replace=True)
        _, p = np.unique(X_sample, axis=0, return_counts=True)
        p = p / len(X_sample)
        h = -np.sum(p * np.log2(p)) / np.log2(len(X_sample))
        result.append(h)
    return result
