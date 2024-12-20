import pandas as pd

# Create the dataset
data = {
    'Product': ['Laptop', 'Mouse', 'Chair', 'Table', 'Headphone'],
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics'],
    'Price': [800, 20, 100, 150, 50],
    'Quantity': [5, 50, 15, 10, 30],
    'Revenue': [4000, 1000, 1500, 1500, 1500]
}

df = pd.DataFrame(data)

# Task 1: Filtering
filtered_price = df[df['Price'] > 100]
filtered_category = df[df['Category'] == 'Furniture']

# Task 2: Sorting
sorted_revenue = df.sort_values(by='Revenue', ascending=False)
sorted_quantity = df.sort_values(by='Quantity', ascending=True)

# Task 3: Aggregation
total_revenue = df['Revenue'].sum()
average_price = df['Price'].mean()

# Task 4: Grouping and Aggregating
grouped_revenue = df.groupby('Category')['Revenue'].sum()
grouped_avg_price = df.groupby('Category')['Price'].mean()

# Display results
print("Filtered by Price > 100:\n", filtered_price)
print("\nFiltered by Category == 'Furniture':\n", filtered_category)
print("\nSorted by Revenue (Descending):\n", sorted_revenue)
print("\nSorted by Quantity (Ascending):\n", sorted_quantity)
print("\nTotal Revenue:", total_revenue)
print("Average Price:", average_price)
print("\nGrouped by Category - Total Revenue:\n", grouped_revenue)
print("\nGrouped by Category - Average Price:\n", grouped_avg_price)
