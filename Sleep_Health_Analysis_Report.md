# SLEEP HEALTH AND LIFESTYLE ANALYSIS

## 1. Introduction

Sleep plays an important role in maintaining human health and overall well-being. Sleep quality and duration can be influenced by several lifestyle factors, including physical activity, stress levels, occupation, age, and daily habits.

This project focuses on analysing sleep health and lifestyle data using Python. The main purpose is to understand the relationship between lifestyle factors and sleep patterns and identify possible trends in sleep disorders.

The project uses Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn for data inspection, cleaning, analysis, and visualization.

## 2. Project Objectives

The main objectives of this project are:

1. To inspect and understand the sleep health dataset.
2. To identify and handle missing values.
3. To identify and remove duplicate records.
4. To perform exploratory data analysis (EDA).
5. To analyse sleep duration and sleep quality.
6. To understand the distribution of sleep disorders.
7. To compare sleep patterns between male and female participants.
8. To visualize the findings using charts and graphs.
9. To identify meaningful insights from the dataset.

## 3. Tools and Technologies Used

- Python
- Visual Studio Code
- Pandas
- NumPy
- Matplotlib
- Seaborn
- CSV Dataset

## 4. Dataset Description

The dataset used in this project is called Sleep Health and Lifestyle Dataset.

It contains information about individuals, their lifestyle habits, sleep patterns, and sleep disorders.

### Dataset Overview

- Total Records: 374
- Total Columns: 13
- File Format: CSV
- Data Source: Sleep Health and Lifestyle Dataset

### Dataset Columns

The dataset contains the following attributes:

1. Person ID
2. Gender
3. Age
4. Occupation
5. Sleep Duration
6. Quality of Sleep
7. Physical Activity Level
8. Stress Level
9. BMI Category
10. Blood Pressure
11. Heart Rate
12. Daily Steps
13. Sleep Disorder

### Dataset Information

The dataset contains numerical and categorical variables.

Numerical variables include Age, Sleep Duration, Quality of Sleep, Stress Level, Heart Rate, and Daily Steps.

Categorical variables include Gender, Occupation, BMI Category, and Sleep Disorder.

The dataset was loaded into Python using the Pandas library for further inspection and analysis.

## 5. Data Cleaning Process

Data cleaning is an important step in data analysis. It helps improve data quality and ensures accurate results.

Python Pandas was used to clean the Sleep Health and Lifestyle dataset.

### 5.1 Initial Data Inspection

The dataset was inspected to identify:
- Missing values
- Duplicate records
- Column names
- Data types
- Dataset structure

### 5.2 Handling Missing Values

During the initial inspection, 219 missing values were identified in the Sleep Disorder column.

These missing values were replaced with "None" to represent participants without a recorded sleep disorder.

### 5.3 Removing Extra Spaces

Extra spaces were removed from column names and text columns using Python string operations.

### 5.4 Duplicate Records

The dataset was checked for duplicate records.

No duplicate rows were found.

### 5.5 Final Data Validation

After cleaning:
- Missing values: 0
- Duplicate rows: 0
- Total records: 374
- Total columns: 13

### 5.6 Saving the Cleaned Dataset

The cleaned dataset was saved as:

sleep_health_cleaned.csv

The cleaned file was stored in the Reports folder for further analysis.

## 6. Data Visualization

Data visualization was performed using Matplotlib and Seaborn libraries.

The following visualizations were created:

1. Sleep Duration Distribution
2. Sleep Disorder Distribution
3. Average Sleep Duration by Gender
4. Stress Level vs Sleep Duration

### 6.1 Sleep Duration Distribution

This chart represents the distribution of sleeping hours among participants.

### 6.2 Sleep Disorder Distribution

This chart compares the number of participants suffering from Sleep Apnea and Insomnia.

### 6.3 Average Sleep Duration by Gender

The analysis shows:
- Female average sleep duration: 7.23 hours
- Male average sleep duration: 7.04 hours

### 6.4 Stress Level vs Sleep Duration

This visualization helps understand the relationship between stress levels and sleep duration.

### Dashboard

![Sleep Health Dashboard](../Visualization/sleep_health_dashboard.png)

## 7. Conclusion

This project successfully analysed sleep health and lifestyle data using Python.

The analysis was performed using Pandas, NumPy, Matplotlib, and Seaborn.

The major findings include:

### Major Findings

1. The dataset contains 374 participants and 13 columns.
2. The average sleep duration is approximately 7.13 hours.
3. The average sleep quality score is approximately 7.31.
4. The average stress level is approximately 5.39.
5. The dataset contains 78 participants with Sleep Apnea and 77 with Insomnia.
6. Female participants had an average sleep duration of 7.23 hours, while male participants had an average of 7.04 hours.
7. The original dataset contained 219 missing values in the Sleep Disorder column and no duplicate records. Missing values were replaced with "None" during cleaning.

### Final Outcome

The project demonstrates how Python can be used to clean, analyse, visualize, and interpret real-world health and lifestyle data.

The completed dashboard provides a visual summary of the analysis and helps communicate important findings.