#!/usr/bin/env python3
"""Module for saving and loading Keras model weights."""


def save_model_weights(model, filepath):
    """
    Save the weights of a trained Keras model.

    Args:
        model: A trained Keras model.
        filepath: Path where the model weights will be saved.

    Returns:
        None.
    """
    model.save_weights(filepath)


def load_model_weights(model, filepath):
    """
    Load saved weights into an existing Keras model.

    Args:
        model: A compatible Keras model.
        filepath: Path from which to load the saved weights.

    Returns:
        None.
    """
    model.load_weights(filepath)
