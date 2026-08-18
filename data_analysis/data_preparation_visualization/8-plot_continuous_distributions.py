#!/usr/bin/env python3
"""
Plot distributions of continuous numerical features.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """
    Plot histogram + KDE and boxplot for continuous columns.
    """

    # Select all numerical columns if none are specified
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(
            include=np.number
        ).columns.tolist()

    n_cols = len(columns_to_plot)

    fig, axes = plt.subplots(
        n_cols,
        2,
        figsize=(10, 3 * n_cols)
    )

    # Ensure axes is always 2-dimensional
    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, column in enumerate(columns_to_plot):

        # Remove missing values
        data = df[column].dropna()

        # -------------------------
        # LEFT: Histogram
        # -------------------------
        axes[i, 0].hist(
            data,
            bins=30,
            density=True,
            alpha=0.7,
            edgecolor="black"
        )

        # KDE calculation
        kde = stats.gaussian_kde(data)

        x_values = np.linspace(
            data.min(),
            data.max(),
            200
        )

        axes[i, 0].plot(
            x_values,
            kde(x_values),
            color="red"
        )

        axes[i, 0].set_title(
            f"{column} Histogram + KDE"
        )

        # -------------------------
        # RIGHT: Boxplot
        # -------------------------
        axes[i, 1].boxplot(
            data,
            vert=False
        )

        axes[i, 1].set_title(
            f"{column} Boxplot"
        )

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()