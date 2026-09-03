#!/usr/bin/env python3
"""Module for evaluating classifier performance."""

from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """
    Generate a classification report for predicted labels.

    Args:
        true_labels: Ground truth labels.
        predicted_labels: Predicted class labels.
        class_names: List of class names corresponding to label indices.

    Returns:
        A string containing the classification report.
    """
    return metrics.classification_report(
        true_labels,
        predicted_labels,
        target_names=class_names
    )