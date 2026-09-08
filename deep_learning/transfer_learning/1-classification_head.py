#!/usr/bin/env python3
"""Add a classification head to a pretrained feature extractor."""

from tensorflow import keras


def add_classification_head(base_model, num_classes):
    """Return a model with a classification head added to base_model."""
    features = base_model.output

    hidden = keras.layers.Dense(
        128,
        activation="relu"
    )(features)

    outputs = keras.layers.Dense(
        num_classes,
        activation="softmax"
    )(hidden)

    model = keras.Model(
        inputs=base_model.input,
        outputs=outputs
    )

    return model
