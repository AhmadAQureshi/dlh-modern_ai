#!/usr/bin/env python3
"""Module for generating predictions with a trained Keras model."""

import tensorflow as tf


def predict(model, X, verbose=0):
    """
    Generate predicted class labels using a trained Keras model.

    Args:
        model: A trained Keras model.
        X: Input data.
        verbose: Verbosity level for prediction.

    Returns:
        Predicted class labels.
    """
    probabilities = model.predict(X, verbose=verbose)
    predictions = tf.argmax(probabilities, axis=1)

    return predictions
