#!/usr/bin/env python3
"""Build a frozen CNN feature extractor using MobileNetV2."""

from tensorflow import keras


def build_feature_extractor():
    """Create and return a frozen MobileNetV2 feature extractor."""
    base_model = keras.applications.MobileNetV2(
        weights="imagenet",
        include_top=False,
        input_shape=(224, 224, 3)
    )

    base_model.trainable = False

    inputs = keras.Input(shape=(224, 224, 3))
    features = base_model(inputs, training=False)
    outputs = keras.layers.GlobalAveragePooling2D()(features)

    model = keras.Model(inputs=inputs, outputs=outputs)

    return model