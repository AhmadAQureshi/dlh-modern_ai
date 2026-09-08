#!/usr/bin/env python3
"""Create an image data augmentation pipeline."""

from tensorflow import keras


def build_data_augmentation():
    """Build and return a Keras image augmentation model."""
    augmentation = keras.Sequential([
        keras.layers.RandomFlip(
            "horizontal",
            seed=42
        ),
        keras.layers.RandomRotation(
            0.15,
            seed=42
        ),
        keras.layers.RandomZoom(
            0.15,
            seed=42
        ),
        keras.layers.RandomContrast(
            0.1,
            seed=42
        )
    ])

    return augmentation
