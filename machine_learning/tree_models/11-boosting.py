#!/usr/bin/env python3
"""Module for creating different boosting classifiers."""

from sklearn import ensemble
import xgboost as xgb
import lightgbm as lgb


def compare_boosting_classifiers(name, n_estimators, random_state):
    """
    Create and return a boosting classifier.

    Args:
        name: Name of the boosting algorithm.
        n_estimators: Number of boosting iterations.
        random_state: Seed for reproducibility.

    Returns:
        An untrained boosting classifier.

    Raises:
        ValueError: If the model name is unknown.
    """
    if name == "adaboost":
        model = ensemble.AdaBoostClassifier(
            n_estimators=n_estimators,
            random_state=random_state
        )

    elif name == "gradientboosting":
        model = ensemble.GradientBoostingClassifier(
            n_estimators=n_estimators,
            random_state=random_state
        )

    elif name == "xgboost":
        model = xgb.XGBClassifier(
            n_estimators=n_estimators,
            random_state=random_state
        )

    elif name == "lightgbm":
        model = lgb.LGBMClassifier(
            n_estimators=n_estimators,
            random_state=random_state,
            verbose=-1
        )

    else:
        raise ValueError(f"Unknown model name '{name}'")

    return model