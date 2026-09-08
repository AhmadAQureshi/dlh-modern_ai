#!/usr/bin/env python3
"""Module for building the MobileNetV1 architecture."""

from tensorflow import keras as K

mobilenet_backbone = __import__(
    '5-mobilenet_backbone'
).mobilenet_backbone


def mobilenet(input_shape=(224, 224, 3), num_classes=1000):
    """
    Build the MobileNetV1 architecture.

    Args:
        input_shape: Shape of the input image.
        num_classes: Number of output classes.

    Returns:
        A Keras Model representing MobileNetV1.
    """
    inputs = K.Input(
        shape=input_shape,
        name='input_layer'
    )

    x = mobilenet_backbone(inputs)

    x = K.layers.GlobalAveragePooling2D(
        name='global_average_pooling'
    )(x)

    outputs = K.layers.Dense(
        num_classes,
        activation='softmax',
        name='predictions'
    )(x)

    model = K.Model(
        inputs=inputs,
        outputs=outputs,
        name='MobileNetV1'
    )

    return model