#!/usr/bin/env python3
"""Module for retrieving feature importance from a random forest."""

import numpy as np


def feature_importance(rf):
    """
    Return feature importance scores and their sorted indices.

    Args:
        rf: A trained RandomForestClassifier instance.

    Returns:
        importances: NumPy array containing feature importance scores.
        indices: Feature indices sorted from least to most important.
    """
    importances = rf.feature_importances_
    indices = np.argsort(importances)

    return importances, indices