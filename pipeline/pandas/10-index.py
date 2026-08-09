#!/usr/bin/env python3
"""Set the Timestamp column as the DataFrame index."""

import pandas as pd


def index(df):
    """Return the DataFrame with Timestamp set as its index."""
    return df.set_index("Timestamp")
