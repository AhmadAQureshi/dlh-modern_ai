#!/usr/bin/env python3
"""Calculate descriptive statistics for a pandas DataFrame."""

import pandas as pd


def analyze(df):
    """Return statistics for every column except Timestamp."""
    return df.drop(columns=["Timestamp"]).describe()
