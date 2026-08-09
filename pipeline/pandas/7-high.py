#!/usr/bin/env python3
"""Sort a pandas DataFrame by its High column."""

import pandas as pd


def high(df):
    """Return the DataFrame sorted by High in descending order."""
    return df.sort_values(by="High", ascending=False)
