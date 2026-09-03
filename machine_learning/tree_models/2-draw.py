#!/usr/bin/env python3
"""Module for displaying the rules of a trained decision tree."""

from sklearn import tree


def draw(clf, feature_names, class_names):
    """
    Display the textual structure of a trained decision tree.

    Args:
        clf: A trained Scikit-learn DecisionTreeClassifier.
        feature_names: List of input feature names.
        class_names: List of target class names.

    Returns:
        None.
    """
    rules = tree.export_text(
        clf,
        feature_names=feature_names,
        class_names=class_names
    )
    print(rules, end="")
