#!/usr/bin/env python3
"""
Convert specified DataFrame columns to appropriate data types.
"""

import pandas as pd


def convert_columns(df):
    """
    Convert TotalCharges to numeric and SeniorCitizen
    from 0/1 to No/Yes.
    """
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df["SeniorCitizen"] = df["SeniorCitizen"].map({
        0: "No",
        1: "Yes"
    })

    return df
