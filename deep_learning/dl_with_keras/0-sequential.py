#!/usr/bin/env python3
"""Module for building a shallow neural network using Keras."""

from tensorflow import keras


def build_model(input_dim, n_h):
    """
    Build a shallow neural network for multi-class classification.

    Args:
        input_dim: Number of input features.
        n_h: Number of neurons in the hidden layer.

    Returns:
        A Keras Sequential model.
    """
    model = keras.Sequential([
        keras.layers.Dense(
            n_h,
            activation='sigmoid',
            input_shape=(input_dim,)
        ),
        keras.layers.Dense(
            10,
            activation='softmax'
        )
    ])

    return model