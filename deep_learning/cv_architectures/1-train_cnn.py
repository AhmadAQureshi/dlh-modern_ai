#!/usr/bin/env python3
"""Module for compiling and training a convolutional neural network."""

from tensorflow import keras


def compile_and_train_cnn(
        model, epochs, batch_size, x_train, y_train,
        x_val, y_val, optimizer_name='adam',
        optimizer_params=None):
    """
    Compile and train a CNN model.

    Args:
        model: CNN model to train.
        epochs: Number of training epochs.
        batch_size: Number of samples in each training batch.
        x_train: Training input images.
        y_train: Training labels.
        x_val: Validation input images.
        y_val: Validation labels.
        optimizer_name: Name of optimizer to use.
        optimizer_params: Additional optimizer parameters.

    Returns:
        The trained model and its training history.
    """
    if optimizer_params is None:
        optimizer_params = {}

    if optimizer_name.lower() == 'adam':
        optimizer = keras.optimizers.Adam(**optimizer_params)
    elif optimizer_name.lower() == 'sgd':
        optimizer = keras.optimizers.SGD(**optimizer_params)
    elif optimizer_name.lower() == 'rmsprop':
        optimizer = keras.optimizers.RMSprop(**optimizer_params)

    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    history = model.fit(
        x_train,
        y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(x_val, y_val),
        verbose=1
    )

    return model, history