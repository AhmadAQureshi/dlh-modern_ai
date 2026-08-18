#!/usr/bin/env python3
"""
Plot correlation heatmap for continuous numerical features.
"""

import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Visualize correlations between numerical features.
    """
    plt.figure(figsize=(6, 5))

    # Select numerical columns and calculate correlations
    correlation = df.select_dtypes(include="number").corr()

    # Create annotated heatmap
    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        vmin=-1,
        vmax=1
    )

    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()
