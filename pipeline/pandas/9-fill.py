#!/usr/bin/env python3
"""Fill missing values in a pandas DataFrame."""

import pandas as pd


def fill(df):
    """Remove Weighted_Price and fill missing values."""
    df = df.drop(columns=["Weighted_Price"])

    # Fill missing Close values using the previous row
    df["Close"] = df["Close"].ffill()

    # Fill missing price values with Close from the same row
    for column in ["High", "Low", "Open"]:
        df[column] = df[column].fillna(df["Close"])

    # Replace missing volume values with zero
    volume_columns = ["Volume_(BTC)", "Volume_(Currency)"]
    df[volume_columns] = df[volume_columns].fillna(0)

    return df
