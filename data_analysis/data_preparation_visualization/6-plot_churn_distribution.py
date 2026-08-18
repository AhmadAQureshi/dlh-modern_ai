#!/usr/bin/env python3
"""
Plot the distribution of the Churn target variable.
"""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Plot the Churn class distribution.
    """
    plt.figure(figsize=(12, 8))

    churn_counts = df["Churn"].value_counts()

    plt.bar(
        churn_counts.index,
        churn_counts.values,
        color=[
            "skyblue" if value == "No" else "salmon"
            for value in churn_counts.index
        ]
    )

    plt.title("Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Count")

    plt.show()
