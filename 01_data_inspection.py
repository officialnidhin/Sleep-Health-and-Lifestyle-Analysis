# SLEEP HEALTH AND LIFESTYLE ANALYSIS

# Step 1: Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset

df = pd.read_csv("Data/Sleep_health_and_lifestyle_dataset.csv")

# Step 3: Display basic information

print("FIRST 5 ROWS:")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nDATASET INFORMATION:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# STEP 4: DATA CLEANING

print("\n========== DATA CLEANING ==========")

# 1. Create a copy of the original dataset
cleaned_df = df.copy()

# 2. Remove extra spaces from column names
cleaned_df.columns = cleaned_df.columns.str.strip()

# 3. Handle missing values in Sleep Disorder
cleaned_df["Sleep Disorder"] = cleaned_df["Sleep Disorder"].fillna("None")

# 4. Remove extra spaces from text columns
for column in cleaned_df.select_dtypes(include="object").columns:
    cleaned_df[column] = cleaned_df[column].str.strip()

# 5. Check missing values after cleaning
print("\nMISSING VALUES AFTER CLEANING:")
print(cleaned_df.isnull().sum())

# 6. Check duplicate rows
print("\nDUPLICATE ROWS AFTER CLEANING:")
print(cleaned_df.duplicated().sum())

# 7. Save cleaned dataset
cleaned_df.to_csv("Reports/sleep_health_cleaned.csv", index=False)

print("\nCLEANED DATASET SAVED SUCCESSFULLY!")