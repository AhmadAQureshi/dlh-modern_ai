#!/usr/bin/env python3
"""Module for building the ResNet-101 architecture."""

from tensorflow import keras as K

bottleneck_block = __import__('2-bottleneck_block').bottleneck_block


def make_layer(x, blocks, filters, stride=1, name=None):
    """
    Build one ResNet stage made of bottleneck blocks.

    Args:
        x: Input tensor.
        blocks: Number of bottleneck blocks.
        filters: Number of filters for the 3x3 convolution.
        stride: Stride used in the first block.
        name: Name prefix for the stage.

    Returns:
        Output tensor after all bottleneck blocks.
    """
    x = bottleneck_block(
        x,
        filters,
        stride=stride,
        downsample=True,
        name=f'{name}_block1'
    )

    for i in range(1, blocks):
        x = bottleneck_block(
            x,
            filters,
            stride=1,
            downsample=False,
            name=f'{name}_block{i + 1}'
        )

    return x


def build_resnet101(input_shape=(224, 224, 3), num_classes=1000):
    """
    Build the ResNet-101 architecture.

    Args:
        input_shape: Shape of the input image.
        num_classes: Number of output classes.

    Returns:
        A Keras ResNet-101 model.
    """
    inputs = K.Input(shape=input_shape, name='input_layer')

    x = K.layers.Conv2D(
        64,
        kernel_size=(7, 7),
        strides=2,
        padding='same',
        use_bias=False,
        name='conv1'
    )(inputs)

    x = K.layers.BatchNormalization(name='bn1')(x)
    x = K.layers.ReLU(name='relu1')(x)

    x = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=2,
        padding='same',
        name='maxpool'
    )(x)

    x = make_layer(
        x,
        blocks=3,
        filters=64,
        stride=1,
        name='layer1'
    )

    x = make_layer(
        x,
        blocks=4,
        filters=128,
        stride=2,
        name='layer2'
    )

    x = make_layer(
        x,
        blocks=23,
        filters=256,
        stride=2,
        name='layer3'
    )

    x = make_layer(
        x,
        blocks=3,
        filters=512,
        stride=2,
        name='layer4'
    )

    x = K.layers.GlobalAveragePooling2D(
        name='avgpool'
    )(x)

    outputs = K.layers.Dense(
        num_classes,
        activation='softmax',
        name='fc'
    )(x)

    model = K.Model(
        inputs=inputs,
        outputs=outputs,
        name='resnet101'
    )

    return model
