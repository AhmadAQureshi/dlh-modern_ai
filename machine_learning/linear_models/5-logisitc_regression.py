#!/usr/bin/env python3
"""Module for creating a logistic regression classifier."""

from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """
    Create and return an untrained Logistic Regression model.

    Args:
        random_state: Integer used as the random seed for reproducibility.

    Returns:
        An untrained LogisticRegression model.
    """
    model = linear_model.LogisticRegression(random_state=random_state)
    return model
