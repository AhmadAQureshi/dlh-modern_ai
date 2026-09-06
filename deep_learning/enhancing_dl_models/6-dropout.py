#!/usr/bin/env python3
"""Module for building a neural network with dropout regularization."""

from tensorflow import keras


def build_model_with_dropout(
        input_dim, hidden_units, n_layers,
        dropout_rate_input, dropout_rate_hidden):
    """
    Build a neural network with dropout regularization.

    Args:
        input_dim: Number of input features.
        hidden_units: Number of neurons in each hidden layer.
        n_layers: Number of hidden layers.
        dropout_rate_input: Dropout rate applied after the input layer.
        dropout_rate_hidden: Dropout rate after each hidden layer.

    Returns:
        A Keras model with dropout regularization.
    """
    model = keras.models.Sequential()

    model.add(keras.layers.Input(shape=(input_dim,)))
    model.add(keras.layers.Dropout(dropout_rate_input))

    for _ in range(n_layers):
        model.add(
            keras.layers.Dense(
                hidden_units,
                activation='relu'
            )
        )
        model.add(
            keras.layers.Dropout(dropout_rate_hidden)
        )

    model.add(
        keras.layers.Dense(
            10,
            activation='softmax'
        )
    )

    return model
