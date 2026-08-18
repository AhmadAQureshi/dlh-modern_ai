#!/usr/bin/env python3
"""
Plot churn distribution.
"""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Plot the distribution of Churn values.
    """
    plt.figure(figsize=(12, 8))

    counts = df["Churn"].value_counts().reindex(["No", "Yes"])

    plt.bar(
        counts.index,
        counts.values,
        color=["skyblue", "salmon"]
    )

    plt.show()
