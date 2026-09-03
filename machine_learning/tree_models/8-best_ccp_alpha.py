#!/usr/bin/env python3
"""Module for selecting the best cost-complexity pruning alpha."""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """
    Select the best ccp_alpha and its corresponding classifier.

    Selection rules:
        1. Highest test accuracy.
        2. If tied, smallest difference between train and test accuracy.
        3. If still tied, largest ccp_alpha.

    Args:
        clfs: List of trained DecisionTreeClassifier instances.
        train_scores: Training accuracy scores.
        test_scores: Testing accuracy scores.
        ccp_alphas: Pruning alpha values.

    Returns:
        best_alpha: Selected ccp_alpha value.
        best_clf: Classifier associated with the selected alpha.
    """
    best_index = max(
        range(len(clfs)),
        key=lambda i: (
            test_scores[i],
            -abs(train_scores[i] - test_scores[i]),
            ccp_alphas[i]
        )
    )

    return ccp_alphas[best_index], clfs[best_index]