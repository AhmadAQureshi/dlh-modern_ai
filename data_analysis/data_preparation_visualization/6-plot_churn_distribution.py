#!/usr/bin/env python3
"""
Plot the distribution of the Churn target variable.
"""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Visualize the distribution of Churn values.
    """
    plt.figure(figsize=(12, 8))

    churn_counts = df["Churn"].value_counts()

    plt.bar(
        churn_counts.index,
        churn_counts.values,
        color=["skyblue" if x == "No" else "salmon"
               for x in churn_counts.index]
    )

    plt.xlabel("Churn")
    plt.ylabel("Count")
    plt.title("Churn Distribution")

    plt.tight_layout()
    plt.show()