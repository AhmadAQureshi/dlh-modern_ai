#!/usr/bin/env python3
"""Module for training a Keras model with TensorBoard logging."""

from tensorflow import keras
import datetime


def log_to_tensorboard(log_dir, model, X, Y, epochs, verbose=1):
    """
    Train a Keras model while logging metrics to TensorBoard.

    Args:
        log_dir: Base directory where TensorBoard logs are saved.
        model: Keras model to train.
        X: Input training data.
        Y: Training labels.
        epochs: Number of training epochs.
        verbose: Verbosity mode.

    Returns:
        None.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = f"{log_dir}/{timestamp}"

    tensorboard_callback = keras.callbacks.TensorBoard(
        log_dir=run_dir,
        histogram_freq=1
    )

    model.fit(
        X,
        Y,
        epochs=epochs,
        verbose=verbose,
        callbacks=[tensorboard_callback]
    )