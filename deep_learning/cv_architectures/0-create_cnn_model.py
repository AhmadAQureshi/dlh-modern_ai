#!/usr/bin/env python3
"""Module for creating a convolutional neural network."""

from tensorflow import keras


def create_cnn_model(
        input_shape, filters, kernel_sizes,
        activations, pooling_type='max'):
    """
    Create a CNN model for multi-class image classification.

    Args:
        input_shape: Shape of the input image.
        filters: Number of filters for each convolutional layer.
        kernel_sizes: Kernel size for each convolutional layer.
        activations: Activation function for each convolutional layer.
        pooling_type: Type of pooling, either 'max' or 'avg'.

    Returns:
        A Keras Sequential CNN model.
    """
    model = keras.models.Sequential()
    model.add(keras.layers.Input(shape=input_shape))

    for filter_count, kernel_size, activation in zip(
            filters, kernel_sizes, activations):
        model.add(
            keras.layers.Conv2D(
                filters=filter_count,
                kernel_size=kernel_size,
                activation=activation
            )
        )

        if pooling_type == 'max':
            model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        elif pooling_type == 'avg':
            model.add(keras.layers.AveragePooling2D(pool_size=(2, 2)))

    model.add(keras.layers.Flatten())
    model.add(
        keras.layers.Dense(
            10,
            activation='softmax'
        )
    )

    return model