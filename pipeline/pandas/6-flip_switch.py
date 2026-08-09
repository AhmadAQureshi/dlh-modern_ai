#!/usr/bin/env python3
"""Reverse and transpose a pandas DataFrame."""

import pandas as pd


def flip_switch(df):
    """Sort rows in reverse order and transpose the DataFrame."""
    return df.sort_index(ascending=False).transpose()
