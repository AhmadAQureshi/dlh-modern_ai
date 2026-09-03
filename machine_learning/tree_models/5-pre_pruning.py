#!/usr/bin/env python3
"""Module for finding optimal pre-pruning hyperparameters."""

from sklearn import model_selection


def prepruning(X, y, clf):
    """
    Find the best pre-pruning parameters for a decision tree.

    Args:
        X: Input features.
        y: Target labels.
        clf: An untrained DecisionTreeClassifier.

    Returns:
        A dictionary containing the best hyperparameters.
    """
    parameters = {
        "criterion": ["gini", "entropy"],
        "max_depth": range(2, 5),
        "min_samples_leaf": range(2, 5),
        "min_samples_split": range(2, 5)
    }

    grid_search = model_selection.GridSearchCV(
        clf,
        parameters
    )

    grid_search.fit(X, y)

    return grid_search.best_params_