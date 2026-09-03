#!/usr/bin/env python3
"""Module for creating a random forest classifier."""

from sklearn import ensemble


def random_forest(n_estimators, random_state):
    """
    Create a random forest classifier.

    Args:
        n_estimators: Number of trees in the forest.
        random_state: Seed for reproducibility.

    Returns:
        A RandomForestClassifier instance.
    """
    model = ensemble.RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )

    return model
