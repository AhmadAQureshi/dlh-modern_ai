#!/usr/bin/env python3
"""Module for building a decision tree classifier."""

from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """
    Create and return a decision tree classifier.

    Args:
        min_samples_leaf (int): Minimum number of samples required
            at a leaf node.
        min_samples_split (int): Minimum number of samples required
            to split an internal node.
        random_state (int): Seed used for reproducibility.

    Returns:
        tree.DecisionTreeClassifier: Configured decision tree classifier.
    """
    model = tree.DecisionTreeClassifier(
        criterion="gini",
        min_samples_leaf=min_samples_leaf,
        min_samples_split=min_samples_split,
        random_state=random_state
    )

    return model