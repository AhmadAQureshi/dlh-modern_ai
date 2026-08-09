#!/usr/bin/env python3
"""Concatenate Coinbase and Bitstamp DataFrames."""

import pandas as pd

index = __import__("10-index").index


def concat(df1, df2):
    """Index, filter, label, and concatenate two DataFrames."""
    df1 = index(df1)
    df2 = index(df2)

    # Keep Bitstamp timestamps up to and including 1417411920
    df2 = df2.loc[:1417411920]

    return pd.concat(
        [df2, df1],
        keys=["bitstamp", "coinbase"]
    )
