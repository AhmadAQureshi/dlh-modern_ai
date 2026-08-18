#!/usr/bin/env python3
"""
Perform Chi-square tests between categorical features and Churn.
"""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Calculate Chi-square p-values for categorical features
    against the target variable Churn.
    """

    results = {}

    # Select categorical columns, excluding the target
    categorical_columns = [
        col for col in df.select_dtypes(include="object").columns
        if col != "Churn"
    ]

    for col in categorical_columns:

        # Create contingency table
        contingency_table = pd.crosstab(
            df[col],
            df["Churn"]
        )

        # Perform Chi-square test
        chi2, p_value, dof, expected = stats.chi2_contingency(
            contingency_table
        )

        # Store only the p-value
        results[col] = p_value

    return results
