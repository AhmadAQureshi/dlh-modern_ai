#!/usr/bin/env python3
import pandas as pd
shape = df.shape
dtypes = df.dtypes
head = df.head()
missing_count = df.isnull().sum()
duplicates = df.duplicated().sum()
print("Shape:", shape)
print("Dtypes:\n", data_types)
print("First rows:\n", head)
print("Missing values:\n", missing_count)
print("Duplicates:", duplicates)
