#!/usr/bin/env python3
"""Module for training and evaluating pruned decision trees."""

from sklearn import tree

train_tree = __import__('1-train').train_tree


def prune_and_evaluate_trees(
        X_train, y_train, X_test, y_test, ccp_alphas,
        random_state, min_samples_leaf, min_samples_split):
    """
    Train and evaluate decision trees using different ccp_alpha values.

    Args:
        X_train: Training input features.
        y_train: Training target labels.
        X_test: Testing input features.
        y_test: Testing target labels.
        ccp_alphas: Cost-complexity pruning alpha values.
        random_state: Seed for reproducibility.
        min_samples_leaf: Minimum samples required at a leaf.
        min_samples_split: Minimum samples required to split a node.

    Returns:
        clfs: List of trained decision tree classifiers.
        train_scores: Training accuracy scores.
        test_scores: Testing accuracy scores.
    """
    clfs = []
    train_scores = []
    test_scores = []

    for ccp_alpha in ccp_alphas:
        clf = tree.DecisionTreeClassifier(
            random_state=random_state,
            min_samples_leaf=min_samples_leaf,
            min_samples_split=min_samples_split,
            ccp_alpha=ccp_alpha
        )

        train_tree(clf, X_train, y_train)

        clfs.append(clf)
        train_scores.append(clf.score(X_train, y_train))
        test_scores.append(clf.score(X_test, y_test))

    return clfs, train_scores, test_scores
