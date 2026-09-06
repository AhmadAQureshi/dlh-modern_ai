#!/usr/bin/env python3
"""Module for searching and returning the best hyperparameters."""


def search_and_return_best_model(
        tuner, x_train, y_train, epochs,
        validation_split, verbose=0):
    """
    Search for the best model hyperparameters.

    Args:
        tuner: A configured Keras Tuner object.
        x_train: Training input data.
        y_train: Training target data.
        epochs: Number of epochs for each trial.
        validation_split: Fraction of training data for validation.
        verbose: Verbosity mode.

    Returns:
        The best HyperParameters object found by the tuner.
    """
    tuner.search(
        x_train,
        y_train,
        epochs=epochs,
        validation_split=validation_split,
        verbose=verbose
    )

    best_hyperparameters = tuner.get_best_hyperparameters(
        num_trials=1
    )[0]

    return best_hyperparameters
