#!/usr/bin/env python3
"""Module for evaluating the optimal number of K-Means clusters."""

from sklearn import metrics

K_Means = __import__('2-k_means').K_Means


def optimal_k(X, max_clusters, random_state):
    """
    Evaluate K-Means clustering for different numbers of clusters.

    Args:
        X (numpy.ndarray): Input data of shape
        (n_samples, n_features).
        max_clusters (int): Maximum number of clusters to evaluate.
        random_state (int): Random seed for reproducibility.

    Returns:
        tuple:
            - list[int]: Cluster numbers evaluated.
            - list[float]: Inertia values.
            - list[float]: Silhouette scores.
    """
    ks = []
    inertia_values = []
    silhouette_values = []

    for k in range(2, max_clusters + 1):
        model = K_Means(
            X,
            n_clusters=k,
            random_state=random_state
        )

        ks.append(k)
        inertia_values.append(model.inertia_)

        score = metrics.silhouette_score(
            X,
            model.labels_
        )
        silhouette_values.append(score)

    return ks, inertia_values, silhouette_values
