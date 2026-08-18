#!/usr/bin/env python3
"""
Compare numerical feature distributions by churn.
"""

import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Plot the distribution of a numerical column
    for Churn = No and Churn = Yes.
    """

    plt.figure(figsize=(12, 8))

    # Separate values based on churn status
    churn_no = df[df["Churn"] == "No"][col]
    churn_yes = df[df["Churn"] == "Yes"][col]

    # Plot both distributions using 30 bins
    plt.hist(
        [churn_no, churn_yes],
        bins=30,
        label=["No", "Yes"]
    )

    # Required title and labels
    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)

    # Legend with title
    plt.legend(title="Churn")

    plt.tight_layout()
    plt.show()