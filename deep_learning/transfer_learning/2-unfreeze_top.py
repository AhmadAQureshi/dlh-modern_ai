#!/usr/bin/env python3
"""Utilities for unfreezing top layers of a pretrained model."""


def unfreeze_top_layers(model, n_layers):
    """Unfreeze the last n_layers of model and keep earlier layers frozen."""
    model.trainable = True

    for layer in model.layers[:-n_layers]:
        layer.trainable = False

    for layer in model.layers[-n_layers:]:
        layer.trainable = True
