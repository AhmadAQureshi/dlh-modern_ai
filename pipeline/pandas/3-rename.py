#!/usr/bin/env python3
"""Rename and convert columns in a pandas DataFrame."""

import pandas as pd


def rename(df):
    """Rename Timestamp, convert it to datetime, and select two columns."""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")

    return df[["Datetime", "Close"]]
