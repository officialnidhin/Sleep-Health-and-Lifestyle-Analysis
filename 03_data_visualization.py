# SLEEP HEALTH AND LIFESTYLE ANALYSIS

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load cleaned dataset
df = pd.read_csv("Reports/sleep_health_cleaned.csv")

# Step 3: Set visualization style
sns.set_theme(style="whitegrid")

# Step 4: Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Chart 1: Sleep Duration Distribution
sns.histplot(data=df, x="Sleep Duration", kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Sleep Duration Distribution")

# Chart 2: Sleep Disorder Distribution
sns.countplot(data=df, x="Sleep Disorder", ax=axes[0, 1])
axes[0, 1].set_title("Sleep Disorder Distribution")

# Chart 3: Sleep Duration by Gender
sns.barplot(data=df, x="Gender", y="Sleep Duration", ax=axes[1, 0])
axes[1, 0].set_title("Average Sleep Duration by Gender")

# Chart 4: Stress Level vs Sleep Duration
sns.scatterplot(data=df, x="Stress Level", y="Sleep Duration", ax=axes[1, 1])
axes[1, 1].set_title("Stress Level vs Sleep Duration")

# Step 5: Adjust layout
plt.tight_layout()

# Step 6: Save dashboard
plt.savefig("Visualization/sleep_health_dashboard.png")

# Step 7: Display dashboard
plt.show()

print("DATA VISUALIZATION COMPLETED SUCCESSFULLY!")