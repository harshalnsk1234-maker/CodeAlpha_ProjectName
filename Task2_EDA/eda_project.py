# ============================================
# Exploratory Data Analysis (EDA) Project
# ============================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# Load Dataset
# --------------------------------------------
# Replace 'data.csv' with your dataset filename

df = pd.read_csv("data.csv")

# --------------------------------------------
# Basic Information
# --------------------------------------------
print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== DATASET SHAPE ==========\n")
print(df.shape)

print("\n========== COLUMN NAMES ==========\n")
print(df.columns)

print("\n========== DATA TYPES ==========\n")
print(df.dtypes)

print("\n========== DATASET INFO ==========\n")
print(df.info())

# --------------------------------------------
# Missing Values
# --------------------------------------------
print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# Visualize Missing Values
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# --------------------------------------------
# Duplicate Records
# --------------------------------------------
print("\n========== DUPLICATE RECORDS ==========\n")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# --------------------------------------------
# Statistical Summary
# --------------------------------------------
print("\n========== STATISTICAL SUMMARY ==========\n")
print(df.describe())

# --------------------------------------------
# Separate Numerical and Categorical Columns
# --------------------------------------------
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

print("\n========== NUMERICAL COLUMNS ==========\n")
print(numerical_cols)

print("\n========== CATEGORICAL COLUMNS ==========\n")
print(categorical_cols)

# --------------------------------------------
# Univariate Analysis
# --------------------------------------------

# Histograms for Numerical Columns
for col in numerical_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()

# Count Plot for Categorical Columns
for col in categorical_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(x=df[col])
    plt.title(f"Count Plot of {col}")
    plt.xticks(rotation=45)
    plt.show()

# --------------------------------------------
# Bivariate Analysis
# --------------------------------------------

# Scatter plots between numerical columns
if len(numerical_cols) >= 2:
    for i in range(len(numerical_cols)-1):
        plt.figure(figsize=(6,4))
        sns.scatterplot(
            x=df[numerical_cols[i]],
            y=df[numerical_cols[i+1]]
        )
        plt.title(f"{numerical_cols[i]} vs {numerical_cols[i+1]}")
        plt.show()

# --------------------------------------------
# Correlation Heatmap
# --------------------------------------------
plt.figure(figsize=(10,6))
correlation = df[numerical_cols].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

# --------------------------------------------
# Boxplots for Outlier Detection
# --------------------------------------------
for col in numerical_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# --------------------------------------------
# Pairplot
# --------------------------------------------
if len(numerical_cols) > 1:
    sns.pairplot(df[numerical_cols])
    plt.show()

# --------------------------------------------
# Group By Analysis (Example)
# --------------------------------------------
if len(categorical_cols) > 0 and len(numerical_cols) > 0:
    group_col = categorical_cols[0]
    num_col = numerical_cols[0]

    print(f"\n========== AVERAGE {num_col} BY {group_col} ==========\n")
    print(df.groupby(group_col)[num_col].mean())

# --------------------------------------------
# Observations Section
# --------------------------------------------
print("\n========== OBSERVATIONS ==========\n")
print("""
1. Checked missing values and duplicates.
2. Analyzed numerical and categorical features.
3. Visualized distributions using histograms.
4. Explored relationships using scatter plots.
5. Detected outliers using boxplots.
6. Analyzed correlations using heatmap.
7. Generated pairplots for deeper insights.
""")

# --------------------------------------------
# Save Cleaned Dataset
# --------------------------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_data.csv'")
print("\nEDA Completed Successfully!")