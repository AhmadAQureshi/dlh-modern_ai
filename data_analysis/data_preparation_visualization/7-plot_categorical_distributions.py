#!/usr/bin/env python3
"""
Plot distributions of categorical columns.
"""

import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Plot bar charts for categorical features.
    """

    if columns_to_plot is None:
        # Select all object columns except the target Churn
        columns_to_plot = [
            col for col in df.select_dtypes(include="object").columns
            if col != "Churn"
        ]
    else:
        columns_to_plot = columns_to_plot

    # 3 plots per row
    n_cols = 3
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(15, 5 * n_rows)
    )

    # Convert axes to a flat list
    axes = axes.flatten()

    # Create one bar chart for each categorical column
    for i, column in enumerate(columns_to_plot):
        df[column].value_counts().plot(
            kind="bar",
            ax=axes[i]
        )

        axes[i].set_title(column)
        axes[i].tick_params(
            axis="x",
            rotation=45
        )

    # Hide unused plots
    for i in range(len(columns_to_plot), len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()