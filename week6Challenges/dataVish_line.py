import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May']
sales = [200, 250, 300, 400, 450]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', color='blue', label='Sales')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales (Units)')
plt.grid(True)
plt.legend()
plt.show()
