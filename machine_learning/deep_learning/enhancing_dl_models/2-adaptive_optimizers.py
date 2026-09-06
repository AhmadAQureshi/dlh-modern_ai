#!/usr/bin/env python3
"""Module for configuring SGD and adaptive optimizers."""

from tensorflow import keras


def get_optimizer(name, learning_rate, momentum, beta_1, beta_2, rho):
    """
    Create and return a configured Keras optimizer.

    Args:
        name: Optimizer name: 'sgd', 'adam', or 'rmsprop'.
        learning_rate: Learning rate for the optimizer.
        momentum: Momentum factor for SGD.
        beta_1: First moment decay rate for Adam.
        beta_2: Second moment decay rate for Adam.
        rho: Decay factor for RMSprop.

    Returns:
        A configured Keras optimizer.
    """
    if name == 'sgd':
        optimizer = keras.optimizers.SGD(
            learning_rate=learning_rate,
            momentum=momentum
        )
    elif name == 'adam':
        optimizer = keras.optimizers.Adam(
            learning_rate=learning_rate,
            beta_1=beta_1,
            beta_2=beta_2
        )
    elif name == 'rmsprop':
        optimizer = keras.optimizers.RMSprop(
            learning_rate=learning_rate,
            rho=rho
        )

    return optimizer