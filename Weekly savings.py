import matplotlib.pyplot as plt

# Data
weeks = [1, 2, 3, 4, 5]
savings = [4000, 5980, 4390, 8010, 3450]

# Create a figure with two subplots side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Line Plot
ax1.plot(weeks, savings, marker='o', color='b')
ax1.set_xlabel('Week number')
ax1.set_ylabel('Savings (in ₹)')
ax1.set_title('My Savings (Line Chart)')
ax1.grid(True, linestyle='--', alpha=0.6)

# Bar Plot
ax2.bar(weeks, savings, color='green', alpha=0.7)
ax2.set_xlabel('Week number')
ax2.set_ylabel('Savings (in ₹)')
ax2.set_title('My Savings (Bar Chart)')
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()