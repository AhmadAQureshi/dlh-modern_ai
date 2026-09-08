#!/usr/bin/env python3
"""Unfreeze the top layers of a pretrained model."""


def unfreeze_top_layers(model, n_layers):
    """Unfreeze the last n layers while keeping earlier layers frozen."""
    for layer in model.layers[:-n_layers]:
        layer.trainable = False

    for layer in model.layers[-n_layers:]:
        layer.trainable = True
