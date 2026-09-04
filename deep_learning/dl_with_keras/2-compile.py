#!/usr/bin/env python3
"""Module for compiling a Keras model."""

from tensorflow import keras


def compile_model(model, learning_rate=0.01):
    """
    Compile a Keras model for training.

    Args:
        model: Keras model to compile.
        learning_rate: Learning rate for SGD. Default is 0.01.

    Returns:
        None.
    """
    optimizer = keras.optimizers.SGD(
        learning_rate=learning_rate
    )

    model.compile(
        optimizer=optimizer,
        loss='binary_crossentropy',
        metrics=['accuracy']
    )