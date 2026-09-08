#!/usr/bin/env python3
"""Module for building a MobileNetV1 feature extraction backbone."""

from tensorflow import keras as K

depthwise_separable_conv = __import__(
    '4-depthwise_separable_conv'
).depthwise_separable_conv


def mobilenet_backbone(inputs):
    """
    Build the feature extraction backbone of MobileNetV1.

    Args:
        inputs: Input tensor.

    Returns:
        Output tensor of the MobileNetV1 backbone.
    """
    x = K.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        strides=2,
        padding='same',
        use_bias=False
    )(inputs)

    x = K.layers.BatchNormalization()(x)
    x = K.layers.ReLU()(x)

    x = depthwise_separable_conv(x, filters=64, stride=1)

    x = depthwise_separable_conv(x, filters=128, stride=2)
    x = depthwise_separable_conv(x, filters=128, stride=1)

    x = depthwise_separable_conv(x, filters=256, stride=2)
    x = depthwise_separable_conv(x, filters=256, stride=1)

    x = depthwise_separable_conv(x, filters=512, stride=2)

    for _ in range(5):
        x = depthwise_separable_conv(
            x,
            filters=512,
            stride=1
        )

    x = depthwise_separable_conv(x, filters=1024, stride=2)
    x = depthwise_separable_conv(x, filters=1024, stride=1)

    return x
