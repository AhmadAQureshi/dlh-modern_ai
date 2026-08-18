#!/usr/bin/env python3
"""
Plots the distribution of the Churn column.
"""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Plot Churn value counts.
    """
    plt.figure(figsize=(12, 8))

    counts = df["Churn"].value_counts()

    colors = [
        "skyblue" if value == "No" else "salmon"
        for value in counts.index
    ]

    counts.plot(
        kind="bar",
        color=colors
    )

    plt.show()
