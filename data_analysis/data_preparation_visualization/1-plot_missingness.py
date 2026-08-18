#!/usr/bin/env python3
"""
Visualize missing values in a pandas DataFrame.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Plot the location of missing values in a DataFrame.
    """
    plt.figure(figsize=(12, 8))

    # Find row and column positions containing missing values
    rows, cols = np.where(df.isnull())

    # Plot each missing value as a vertical bar
    plt.scatter(rows, cols, marker='|')

    # Map y-axis positions to DataFrame column names
    plt.yticks(
        range(len(df.columns)),
        df.columns
    )

    plt.title("Missingness Plot")

    plt.tight_layout()
    plt.show()