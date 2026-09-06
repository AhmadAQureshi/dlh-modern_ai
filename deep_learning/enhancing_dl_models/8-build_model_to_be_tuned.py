#!/usr/bin/env python3
"""Module for building a tunable Keras model."""

from tensorflow import keras


def build_model(hp):
    """
    Build and compile a Keras model for hyperparameter tuning.

    Args:
        hp: Keras Tuner HyperParameters object.

    Returns:
        A compiled Keras Sequential model.
    """
    num_layers = hp.Int(
        'num_layers',
        min_value=1,
        max_value=2,
        step=1
    )

    units = hp.Int(
        'units',
        min_value=4,
        max_value=12,
        step=4
    )

    activation = hp.Choice(
        'activation',
        values=['relu', 'sigmoid']
    )

    learning_rate = hp.Choice(
        'learning_rate',
        values=[1e-2, 1e-3]
    )

    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(784,)))

    for _ in range(num_layers):
        model.add(
            keras.layers.Dense(
                units,
                activation=activation
            )
        )

    model.add(
        keras.layers.Dense(
            10,
            activation='softmax'
        )
    )

    optimizer = keras.optimizers.Adam(
        learning_rate=learning_rate
    )

    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model
