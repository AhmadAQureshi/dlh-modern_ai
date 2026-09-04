#!/usr/bin/env python3
"""Module for building a deep neural network."""

from tensorflow import keras


def build_deep_model(input_dim, hidden_layers):
    """
    Build a deep neural network for multi-class classification.

    Args:
        input_dim: Number of input features.
        hidden_layers: List containing the number of neurons
                       in each hidden layer.

    Returns:
        A Keras Sequential model.
    """
    model = keras.Sequential()

    model.add(
        keras.layers.Dense(
            hidden_layers[0],
            activation='relu',
            input_shape=(input_dim,)
        )
    )

    for neurons in hidden_layers[1:]:
        model.add(
            keras.layers.Dense(
                neurons,
                activation='relu'
            )
        )

    model.add(
        keras.layers.Dense(
            10,
            activation='softmax'
        )
    )

    return model
