import matplotlib.pyplot as plt
profits = [500, 650, 800, 950, 1200]
# Data
months = ['January', 'February', 'March', 'April', 'May']
sales = [200, 250, 300, 400, 450]

# Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(months, profits, color='green', label='Profit')
plt.title('Monthly Profit')
plt.xlabel('Month')
plt.ylabel('Profit ($)')
plt.legend()
plt.show()
