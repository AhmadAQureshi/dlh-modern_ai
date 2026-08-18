#!/usr/bin/env python3
"""
Plot churn rate for a categorical feature.
"""

import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """
    Plot churn rate for each category.
    """

    churn_rate = (
        df.groupby(col)["Churn"]
        .apply(lambda x: (x == "Yes").mean())
    )

    plt.figure(figsize=(12, 8))

    plt.bar(
        churn_rate.index,
        churn_rate.values
    )

    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)

    plt.show()
