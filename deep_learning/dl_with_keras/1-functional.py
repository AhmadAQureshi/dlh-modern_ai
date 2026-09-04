#!/usr/bin/env python3
"""Module for building a neural network using the Keras Functional API."""

from tensorflow import keras


def build_model(input_dim, neurons_h):
    """
    Build a shallow neural network using the Functional API.

    Args:
        input_dim: Number of input features.
        neurons_h: Number of neurons in the hidden layer.

    Returns:
        A Keras model.
    """
    inputs = keras.Input(shape=(input_dim,))
    hidden = keras.layers.Dense(
        neurons_h,
        activation='sigmoid'
    )(inputs)
    outputs = keras.layers.Dense(
        10,
        activation='softmax'
    )(hidden)

    model = keras.Model(inputs=inputs, outputs=outputs)

    return model
