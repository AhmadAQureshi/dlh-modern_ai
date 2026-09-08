#!/usr/bin/env python3
"""Module implementing a ResNet bottleneck residual block."""

from tensorflow import keras as K


def bottleneck_block(
        x, filters, stride=1, downsample=False, name=None):
    """
    Create a ResNet bottleneck residual block.

    Args:
        x: Input tensor.
        filters: Number of filters in the 3x3 convolution.
        stride: Stride for the first convolution.
        downsample: Whether to use a projection shortcut.
        name: Optional prefix for layer names.

    Returns:
        Output tensor of the bottleneck residual block.
    """
    prefix = f"{name}_" if name else ""

    shortcut = x

    y = K.layers.Conv2D(
        filters,
        kernel_size=(1, 1),
        strides=stride,
        padding='same',
        use_bias=False,
        name=prefix + "conv1"
    )(x)

    y = K.layers.BatchNormalization(
        name=prefix + "bn1"
    )(y)

    y = K.layers.ReLU(
        name=prefix + "relu1"
    )(y)

    y = K.layers.Conv2D(
        filters,
        kernel_size=(3, 3),
        strides=1,
        padding='same',
        use_bias=False,
        name=prefix + "conv2"
    )(y)

    y = K.layers.BatchNormalization(
        name=prefix + "bn2"
    )(y)

    y = K.layers.ReLU(
        name=prefix + "relu2"
    )(y)

    y = K.layers.Conv2D(
        filters * 4,
        kernel_size=(1, 1),
        strides=1,
        padding='same',
        use_bias=False,
        name=prefix + "conv3"
    )(y)

    y = K.layers.BatchNormalization(
        name=prefix + "bn3"
    )(y)

    if downsample:
        shortcut = K.layers.Conv2D(
            filters * 4,
            kernel_size=(1, 1),
            strides=stride,
            padding='same',
            use_bias=False,
            name=prefix + "shortcut_conv"
        )(shortcut)

        shortcut = K.layers.BatchNormalization(
            name=prefix + "shortcut_bn"
        )(shortcut)

    y = K.layers.Add(
        name=prefix + "add"
    )([y, shortcut])

    y = K.layers.ReLU(
        name=prefix + "out"
    )(y)

    return y
