#!/usr/bin/env python3
"""Module for saving and loading Keras models."""

from tensorflow import keras


def save_model(model, filepath):
    """
    Save a Keras model to a file.

    Args:
        model: A trained Keras model.
        filepath: Path where the model will be saved.

    Returns:
        None.
    """
    model.save(filepath)


def load_model(filepath):
    """
    Load a saved Keras model.

    Args:
        filepath: Path of the saved Keras model.

    Returns:
        The loaded Keras model.
    """
    model = keras.models.load_model(filepath)
    return model
