#!/usr/bin/env python3
"""Slice selected columns of a pandas DataFrame."""

import pandas as pd


def slice(df):
    """Return every 60th row from the required columns."""
    columns = ["High", "Low", "Close", "Volume_(BTC)"]
    return df[columns].iloc[::60]
