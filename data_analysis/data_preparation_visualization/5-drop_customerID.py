#!/usr/bin/env python3
"""
Remove the customerID column from a DataFrame.
"""


def drop_customerID(df):
    """
    Drop the customerID column because it is a unique identifier
    and does not provide predictive value.
    """
    return df.drop(columns=["customerID"])