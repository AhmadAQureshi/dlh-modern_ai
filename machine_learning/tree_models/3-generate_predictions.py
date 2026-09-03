#!/usr/bin/env python3
"""Module for generating predictions with a trained classifier."""


def generate_predictions(clf, X):
    """
    Generate class predictions using a trained classifier.

    Args:
        clf: A trained Scikit-learn classifier instance.
        X: Feature matrix containing input samples.

    Returns:
        A NumPy array containing the predicted class labels.
    """
    return clf.predict(X)
