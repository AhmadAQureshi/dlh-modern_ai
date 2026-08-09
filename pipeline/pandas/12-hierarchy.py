#!/usr/bin/env python3
"""Concatenate DataFrames using a Timestamp-first MultiIndex."""

import pandas as pd

index = __import__("10-index").index


def hierarchy(df1, df2):
    """Combine Coinbase and Bitstamp data in chronological order."""
    df1 = index(df1)
    df2 = index(df2)

    start = 1417411980
    end = 1417417980

    coinbase = df1.loc[start:end]
    bitstamp = df2.loc[start:end]

    df = pd.concat(
        [bitstamp, coinbase],
        keys=["bitstamp", "coinbase"]
    )

    return df.swaplevel(0, 1).sort_index()
