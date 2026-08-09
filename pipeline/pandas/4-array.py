#!/usr/bin/env python3
"""Convert selected DataFrame values to a NumPy array."""

import pandas as pd


def array(df):
    """Return the last 10 High and Close values as a NumPy array."""
    return df[["High", "Close"]].tail(10).to_numpy()
