#!/usr/bin/env python3
"""Unfreeze selected top layers of a pretrained base model."""


def unfreeze_top_layers(model, n_layers):
    """Unfreeze the last n layers of the base model."""
    base_model = model.layers[1]

    for layer in base_model.layers[:-n_layers]:
        layer.trainable = False

    for layer in base_model.layers[-n_layers:]:
        layer.trainable = True
