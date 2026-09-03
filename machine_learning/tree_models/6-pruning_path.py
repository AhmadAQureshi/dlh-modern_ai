#!/usr/bin/env python3
"""Module for retrieving the cost-complexity pruning path."""

def get_pruning_path(clf, X, y):
    """
    Retrieve the cost-complexity pruning path of a decision tree.

    Args:
        clf: A DecisionTreeClassifier instance.
        X: Input features.
        y: Target labels.

    Returns:
        ccp_alphas: Effective alpha values for pruning.
        impurities: Total leaf impurity for each alpha.
    """
    path = clf.cost_complexity_pruning_path(X, y)

    return path.ccp_alphas, path.impurities
