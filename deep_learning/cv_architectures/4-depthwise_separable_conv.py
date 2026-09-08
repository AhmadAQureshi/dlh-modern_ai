#!/usr/bin/env python3
"""Module implementing a depthwise separable convolution block."""

from tensorflow import keras as K


def depthwise_separable_conv(X, filters, stride=1):
    """
    Create a depthwise separable convolution block.

    Args:
        X: Input tensor.
        filters: Number of output filters for pointwise convolution.
        stride: Stride for the depthwise convolution.

    Returns:
        Output tensor of the depthwise separable convolution block.
    """
    Y = K.layers.DepthwiseConv2D(
        kernel_size=(3, 3),
        strides=stride,
        padding='same',
        use_bias=False
    )(X)

    Y = K.layers.BatchNormalization()(Y)
    Y = K.layers.ReLU()(Y)

    Y = K.layers.Conv2D(
        filters=filters,
        kernel_size=(1, 1),
        strides=1,
        padding='same',
        use_bias=False
    )(Y)

    Y = K.layers.BatchNormalization()(Y)
    Y = K.layers.ReLU()(Y)

    return Y