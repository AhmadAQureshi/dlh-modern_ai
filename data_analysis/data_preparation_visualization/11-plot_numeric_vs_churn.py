#!/usr/bin/env python3
"""
Plot numeric feature distribution by churn.
"""

import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Compare a numeric feature for Churn No and Yes.
    """
    plt.figure(figsize=(12, 8))

    churn_no = df[df["Churn"] == "No"][col]
    churn_yes = df[df["Churn"] == "Yes"][col]

    plt.hist(
        [churn_no, churn_yes],
        bins=30,
        label=["No", "Yes"]
    )

    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title="Churn")

    plt.show()
