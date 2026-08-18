#!/usr/bin/env python3
"""
Create NumServices and TenureGroup features.
"""

import pandas as pd


def create_features(df):
    """
    Create engineered features and drop the original columns.
    """

    service_cols = [
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    # Number of subscribed services
    df["NumServices"] = (df[service_cols] == "Yes").sum(axis=1)

    # DSL and Fiber optic both count as an Internet service
    df["NumServices"] += (
        df["InternetService"]
        .isin(["DSL", "Fiber optic"])
        .astype(int)
    )

    # Create tenure categories
    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 60, float("inf")],
        labels=["0-12", "13-24", "25-48", "49-60", "60+"],
        right=True
    )

    # Drop columns used to create the new features
    df.drop(
        columns=service_cols + ["InternetService", "tenure"],
        inplace=True
    )

    return df
