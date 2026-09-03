#!/usr/bin/env python3
"""Module for creating a Lasso regression model."""

from sklearn import linear_model


def lasso_regression(random_state):
    """
    Create and return an untrained Lasso regression model.

    Args:
        random_state: Integer used as the random seed for reproducibility.

    Returns:
        An untrained Lasso regression model.
    """
    model = linear_model.Lasso(random_state=random_state)
    return model