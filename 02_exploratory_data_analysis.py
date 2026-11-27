
# SLEEP HEALTH AND LIFESTYLE ANALYSIS
# STEP 5: EXPLORATORY DATA ANALYSIS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("Reports/sleep_health_cleaned.csv")

print("========== EXPLORATORY DATA ANALYSIS ==========")

# 1. Statistical Summary
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

# 2. Average Sleep Duration
print("\nAVERAGE SLEEP DURATION:")
print(df["Sleep Duration"].mean())

# 3. Average Quality of Sleep
print("\nAVERAGE QUALITY OF SLEEP:")
print(df["Quality of Sleep"].mean())

# 4. Average Stress Level
print("\nAVERAGE STRESS LEVEL:")
print(df["Stress Level"].mean())

# 5. Gender Distribution
print("\nGENDER DISTRIBUTION:")
print(df["Gender"].value_counts())

# 6. Sleep Disorder Distribution
print("\nSLEEP DISORDER DISTRIBUTION:")
print(df["Sleep Disorder"].value_counts())

# 7. Average Sleep Duration by Gender
print("\nSLEEP DURATION BY GENDER:")
print(df.groupby("Gender")["Sleep Duration"].mean())

print("\nEDA ANALYSIS COMPLETED SUCCESSFULLY!")
