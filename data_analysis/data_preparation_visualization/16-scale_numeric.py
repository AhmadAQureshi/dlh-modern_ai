#!/usr/bin/env python3
"""
Scale continuous numeric features using StandardScaler.
"""

from sklearn import preprocessing


def scale_numeric(df):
    """
    Standardize MonthlyCharges and TotalCharges
    so they have approximately mean=0 and std=1.
    """

    df = df.copy()

    scaler = preprocessing.StandardScaler()

    columns_to_scale = [
        "MonthlyCharges",
        "TotalCharges"
    ]

    df[columns_to_scale] = scaler.fit_transform(
        df[columns_to_scale]
    )

    return df
