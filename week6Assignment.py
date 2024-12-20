# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset
    dataset = pd.read_csv("sample_data.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset not found. Ensure the file path is correct.")
    exit()

# Display the first few rows
print("First 5 rows of the dataset:")
print(dataset.head())

# Check the structure of the dataset
print("\nDataset Information:")
print(dataset.info())

# Check for missing values
print("\nMissing Values in Each Column:")
print(dataset.isnull().sum())

# Handle missing values by dropping rows with missing data
dataset = dataset.dropna()
print("\nDataset after dropping missing values:")
print(dataset.info())

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistics of Numerical Columns:")
print(dataset.describe())

# Group by Category and compute mean of Value
grouped_data = dataset.groupby('Category')['Value'].mean()
print("\nAverage Value by Category:")
print(grouped_data)

# Observations
print("\nInteresting Findings:")
print("- Categories with higher average values indicate areas of interest.")
print("- The Value column shows a wide range, as seen in the statistics.")

# Task 3: Data Visualization
# Line Chart: Trends over time
plt.figure(figsize=(10, 5))
plt.plot(dataset['Date'], dataset['Value'], marker='o', label='Value Over Time')
plt.title("Line Chart: Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart: Average Value by Category
plt.figure(figsize=(8, 5))
grouped_data.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Bar Chart: Average Value by Category")
plt.xlabel("Category")
plt.ylabel("Average Value")
plt.show()

# Histogram: Distribution of Value
plt.figure(figsize=(8, 5))
plt.hist(dataset['Value'], bins=20, color='green', edgecolor='black')
plt.title("Histogram: Distribution of Value")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Metric1 vs Metric2
plt.figure(figsize=(8, 5))
plt.scatter(dataset['Metric1'], dataset['Metric2'], alpha=0.7, color='purple')
plt.title("Scatter Plot: Metric1 vs Metric2")
plt.xlabel("Metric1")
plt.ylabel("Metric2")
plt.grid(True)
plt.show()
