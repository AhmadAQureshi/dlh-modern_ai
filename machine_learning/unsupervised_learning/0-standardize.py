#!/usr/bin/env python3
"""Feature standardization module."""

from sklearn import preprocessing


def Standardize(X):
    """Standardize the features in X."""
    return preprocessing.StandardScaler().fit_transform(X)
