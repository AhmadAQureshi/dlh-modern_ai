#!/usr/bin/env python3
"""
Handle missing values in the TotalCharges column.
"""


def clean_total_charges(df, method='drop'):
    """
    Handle missing TotalCharges values using the selected method.
    """

    df = df.copy()

    if method == 'drop':
        # Remove rows where TotalCharges is missing
        df = df.dropna(subset=['TotalCharges'])

    elif method == 'median':
        # Replace missing values with median TotalCharges
        median = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median)

    elif method == 'impute':
        # Estimate TotalCharges using MonthlyCharges * tenure
        missing = df['TotalCharges'].isna()

        df.loc[missing, 'TotalCharges'] = (
            df.loc[missing, 'MonthlyCharges']
            * df.loc[missing, 'tenure']
        )

    return df
