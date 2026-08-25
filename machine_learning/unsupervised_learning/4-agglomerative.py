#!/usr/bin/env python3
"""Module for Agglomerative Hierarchical Clustering."""

from sklearn import cluster
from sklearn import metrics

Apply_PCA = __import__('1-pca').Apply_PCA


def Agglomerative_Clustering(
        X,
        n_clusters,
        random_state,
        n_components,
        use_pca_data=True):
    """
    Perform Agglomerative Hierarchical Clustering.

    Args:
        X (numpy.ndarray): Input data.
        n_clusters (int): Number of clusters.
        random_state (int): Random seed.
        n_components (int): Number of PCA components.
        use_pca_data (bool): Whether PCA should be applied.

    Returns:
        tuple:
            - fitted AgglomerativeClustering model
            - data used for clustering
            - silhouette score
    """

    if use_pca_data:
        X_used, _ = Apply_PCA(
            X,
            n_components=n_components,
            random_state=random_state
        )
    else:
        X_used = X

    model = cluster.AgglomerativeClustering(
        n_clusters=n_clusters,
        linkage='ward'
    )

    labels = model.fit_predict(X_used)

    if n_clusters > 1:
        score = metrics.silhouette_score(
            X_used,
            labels
        )
    else:
        score = None

    return model, X_used, score
