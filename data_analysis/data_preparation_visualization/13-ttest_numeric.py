#!/usr/bin/env python3
"""
Perform Welch's t-tests for continuous numeric features.
"""

from scipy import stats


def ttest_numeric(df):
    """
    Compare numeric features between Churn=Yes and Churn=No groups.
    Returns a dictionary of p-values.
    """

    results = {}

    # Select all numerical columns
    numeric_columns = df.select_dtypes(include="number").columns

    for col in numeric_columns:

        # Separate the two churn groups
        churn_yes = df[df["Churn"] == "Yes"][col].dropna()
        churn_no = df[df["Churn"] == "No"][col].dropna()

        # Welch's t-test
        t_stat, p_value = stats.ttest_ind(
            churn_yes,
            churn_no,
            equal_var=False
        )

        results[col] = p_value

    return results