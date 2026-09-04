#!/usr/bin/env python3
"""Module for training a Keras model."""


def train_model(model, X, Y, epochs, verbose=1):
    """
    Train a Keras model.

    Args:
        model: Keras model to train.
        X: Input training data.
        Y: Training labels.
        epochs: Number of training epochs.
        verbose: Verbosity mode. Default is 1.

    Returns:
        None.
    """
    model.fit(
        X,
        Y,
        epochs=epochs,
        verbose=verbose
    )
