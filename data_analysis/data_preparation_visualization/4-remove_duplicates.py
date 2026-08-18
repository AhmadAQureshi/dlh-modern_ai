#!/usr/bin/env python3
"""
Remove duplicate rows from a DataFrame.
"""


def remove_duplicates(df):
    """
    Remove all duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()
