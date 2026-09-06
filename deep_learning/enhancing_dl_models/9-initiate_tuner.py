#!/usr/bin/env python3
"""Module for initializing Keras Tuner objects."""

import keras_tuner


def initiate_tuner(
        tuner_type, build_model, seed, hyperband_iterations,
        max_trials, objective='val_accuracy', overwrite=True):
    """
    Initialize a Keras Tuner.

    Args:
        tuner_type: Type of tuner to create.
        build_model: Function that builds the Keras model.
        seed: Random seed.
        hyperband_iterations: Number of Hyperband iterations.
        max_trials: Maximum number of trials for RandomSearch
                    and BayesianOptimization.
        objective: Metric to optimize.
        overwrite: Whether to overwrite previous tuner results.

    Returns:
        A configured Keras Tuner object.
    """
    if tuner_type == 'Hyperband':
        tuner = keras_tuner.Hyperband(
            build_model,
            objective=objective,
            hyperband_iterations=hyperband_iterations,
            seed=seed,
            overwrite=overwrite
        )

    elif tuner_type == 'RandomSearch':
        tuner = keras_tuner.RandomSearch(
            build_model,
            objective=objective,
            max_trials=max_trials,
            seed=seed,
            overwrite=overwrite
        )

    elif tuner_type == 'BayesianOptimization':
        tuner = keras_tuner.BayesianOptimization(
            build_model,
            objective=objective,
            max_trials=max_trials,
            seed=seed,
            overwrite=overwrite
        )

    return tuner