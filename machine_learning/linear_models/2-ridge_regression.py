#!/usr/bin/env python3
"""Module for creating a Ridge regression model."""

from sklearn import linear_model


def ridge_regression(random_state):
    """
    Create and return an untrained Ridge regression model.

    Args:
        random_state: Integer used as the random seed for reproducibility.

    Returns:
        An untrained Ridge regression model.
    """
    model = linear_model.Ridge(random_state=random_state)
    return model
