#!/usr/bin/env python3
"""Module for evaluating a trained Keras model."""


def evaluate_model(model, X, Y, verbose=0):
    """
    Evaluate a trained Keras model.

    Args:
        model: A trained Keras model.
        X: Input data.
        Y: True labels.
        verbose: Verbosity mode. Default is 0.

    Returns:
        The loss and accuracy of the model.
    """
    loss, accuracy = model.evaluate(
        X,
        Y,
        verbose=verbose
    )

    return loss, accuracy
