#!/usr/bin/env python3
"""Module for creating a linear regression model."""

from sklearn import linear_model


def Linear_Regression():
    """Create and return an untrained linear regression model."""
    model = linear_model.LinearRegression()
    return model
