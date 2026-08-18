#!/usr/bin/env python3
"""
Plot churn rate for each category of a categorical feature.
"""

import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """
    Plot the proportion of Churn='Yes' for each category.
    """

    # Calculate churn rate for each category
    churn_rate = df.groupby(col)["Churn"].apply(
        lambda x: (x == "Yes").mean()
    )

    # Create figure
    plt.figure(figsize=(12, 8))

    # Plot churn rate
    churn_rate.plot(kind="bar")

    # Labels and title
    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")

    # Rotate x-axis labels
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()