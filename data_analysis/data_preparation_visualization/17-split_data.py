#!/usr/bin/env python3
"""
Split dataset into training and testing sets.
"""

from sklearn import model_selection


def split_data(df, target="Churn", test_size=0.2, random_state=42):
    """
    Split data into train and test sets using stratified sampling.
    """

    # Separate features and target
    X = df.drop(columns=[target])
    y = df[target]

    # Stratified train/test split
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    return X_train, X_test, y_train, y_test