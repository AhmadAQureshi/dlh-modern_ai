#!/usr/bin/env python3
"""Module for applying Principal Component Analysis."""

from sklearn import decomposition


def Apply_PCA(X, n_components, random_state):
    """
    Apply Principal Component Analysis to tabular data.

    Args:
        X (numpy.ndarray): Input data.
        n_components (int, float, or None): Number of components
        or fraction of variance to preserve.
        random_state (int): Random seed.

    Returns:
        tuple: Transformed data and fitted PCA object.
    """
    pca = decomposition.PCA(
        n_components=n_components,
        random_state=random_state
    )

    X_pca = pca.fit_transform(X)

    return X_pca, pca