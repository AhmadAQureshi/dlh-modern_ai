#!/usr/bin/env python3
"""Module for training a tree-based classifier."""


def train_tree(clf, X, y):
    """
    Train a tree-based classifier.

    Args:
        clf: A Scikit-learn classifier instance.
        X: Input features.
        y: Target labels.

    Returns:
        None.
    """
    clf.fit(X, y)