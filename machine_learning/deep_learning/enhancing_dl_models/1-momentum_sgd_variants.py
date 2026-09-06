#!/usr/bin/env python3
"""Module for configuring momentum-based SGD optimizer variants."""

from tensorflow import keras


def get_optimizer_SGD(name, lr, momentum=0.0, nesterov=False):
    """
    Create an SGD optimizer according to the selected variant.

    Args:
        name: Optimizer variant: 'SGD', 'SGD+Momentum',
              or 'SGD+Momentum+Nesterov'.
        lr: Learning rate.
        momentum: Momentum factor.
        nesterov: Whether to apply Nesterov acceleration.

    Returns:
        A configured Keras SGD optimizer.
    """
    if name == 'SGD':
        optimizer = keras.optimizers.SGD(
            learning_rate=lr
        )

    elif name == 'SGD+Momentum':
        optimizer = keras.optimizers.SGD(
            learning_rate=lr,
            momentum=momentum
        )

    elif name == 'SGD+Momentum+Nesterov':
        optimizer = keras.optimizers.SGD(
            learning_rate=lr,
            momentum=momentum,
            nesterov=nesterov
        )

    return optimizer