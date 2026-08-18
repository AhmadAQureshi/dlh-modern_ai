#!/usr/bin/env python3
"""
Encode categorical features for machine learning.
"""

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """
    Encode categorical features and return the encoded DataFrame
    together with the fitted encoders.
    """

    df = df.copy()

    # -------------------------------------------------
    # 1. Encode target: Churn
    # No = 0, Yes = 1
    # -------------------------------------------------
    churn_le = preprocessing.LabelEncoder()
    df["Churn"] = churn_le.fit_transform(df["Churn"])

    # -------------------------------------------------
    # 2. Encode binary categorical columns
    # No = 0, Yes = 1
    # -------------------------------------------------
    binary_cols = [
        "Partner",
        "Dependents",
        "PaperlessBilling",
        "SeniorCitizen"
    ]

    binary_oe = preprocessing.OrdinalEncoder(
        categories=[["No", "Yes"]] * len(binary_cols)
    )

    df[binary_cols] = (
        binary_oe
        .fit_transform(df[binary_cols])
        .astype(int)
    )

    # -------------------------------------------------
    # 3. Encode TenureGroup in alphabetical order
    # -------------------------------------------------
    tenure_oe = preprocessing.OrdinalEncoder()

    df[["TenureGroup"]] = (
        tenure_oe
        .fit_transform(df[["TenureGroup"]])
        .astype(int)
    )

    # -------------------------------------------------
    # 4. One-hot encode Contract and PaymentMethod
    # drop_first=True
    # -------------------------------------------------
    df = pd.get_dummies(
        df,
        columns=["Contract", "PaymentMethod"],
        drop_first=True,
        dtype=int
    )

    return df, churn_le, binary_oe, tenure_oe
