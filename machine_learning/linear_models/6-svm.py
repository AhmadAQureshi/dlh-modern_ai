#!/usr/bin/env python3
"""Module for creating SVM classifiers with different kernels."""

from sklearn import svm


def get_SVM_model(name, random_state):
    """
    Create and return an untrained SVM classifier.

    Args:
        name: Kernel type: 'linear', 'poly', or 'rbf'.
        random_state: Random seed for reproducibility.

    Returns:
        An untrained SVC model.
    """
    model = svm.SVC(
        kernel=name,
        random_state=random_state
    )

    return model
