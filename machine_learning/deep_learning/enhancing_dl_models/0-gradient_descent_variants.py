#!/usr/bin/env python3
"""Module for configuring different gradient descent variants."""

from tensorflow import keras


def train_with_gradient_descent_variant(
        variant, learning_rate, x_train, batch_size):
    """
    Configure an SGD optimizer and batch size.

    Args:
        variant: Gradient descent variant:
            'batch', 'stochastic', or 'mini_batch'.
        learning_rate: Learning rate for the optimizer.
        x_train: Training input data.
        batch_size: Batch size used for mini-batch gradient descent.

    Returns:
        tuple: The configured SGD optimizer and appropriate batch size.
    """
    optimizer = keras.optimizers.SGD(
        learning_rate=learning_rate
    )

    if variant == 'batch':
        bs = x_train.shape[0]
    elif variant == 'stochastic':
        bs = 1
    elif variant == 'mini_batch':
        bs = batch_size

    return optimizer, bs