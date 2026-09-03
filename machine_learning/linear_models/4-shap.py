#!/usr/bin/env python3
"""Module for generating SHAP model explanations."""

import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """
    Create a SHAP explainer and calculate SHAP values.

    Args:
        model: A trained regression model.
        X_train: Training data used as the background dataset.
        X_test: Test data to explain.

    Returns:
        tuple: The SHAP explainer and SHAP values for X_test.
    """
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)

    return explainer, shap_values
