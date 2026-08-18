#!/usr/bin/env python3
"""
Plot correlation heatmap for numerical features.
"""

import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Plot an annotated correlation heatmap.
    """
    plt.figure(figsize=(6, 5))

    correlation = df.corr(numeric_only=True)

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        vmin=-1,
        vmax=1
    )

    plt.title("Correlation Matrix")
    plt.show()
