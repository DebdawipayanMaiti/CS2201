import matplotlib.pyplot as plt

# User input for months and rainfall
months = list(map(int, input("Enter months (space-separated): ").split()))
rainfall = list(map(float, input("Enter rainfall (mm) (space-separated): ").split()))

# Plot
plt.figure(figsize=(8, 5))
plt.plot(months, rainfall, marker='o', linestyle='-', color='b', label="Rainfall (mm)")

# Labels and title
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall")
plt.legend()
plt.grid(True)
plt.show()




temperature = list(map(float, input("Enter temperature (°C) (space-separated): ").split()))
plt.figure(figsize=(8, 5))
plt.plot(months, rainfall, marker='o', linestyle='-', color='b', label="Rainfall (mm)")
plt.plot(months, temperature, marker='s', linestyle='--', color='r', label="Temperature (°C)")
plt.xlabel("Months")
plt.ylabel("Values")
plt.title("Rainfall and Temperature Trends")
plt.legend()
plt.grid(True)
plt.show()

fig, axes = plt.subplots(2, 1, figsize=(6, 8))  # 2 rows, 1 column
axes[0].plot(months, rainfall, marker='o', linestyle='-', color='b', label="Rainfall (mm)")
axes[0].set_title("Monthly Rainfall")
axes[0].set_xlabel("Months")
axes[0].set_ylabel("Rainfall (mm)")
axes[0].legend()
axes[0].grid(True)
axes[1].plot(months, temperature, marker='s', linestyle='--', color='r', label="Temperature (°C)")
axes[1].set_title("Monthly Temperature")
axes[1].set_xlabel("Months")
axes[1].set_ylabel("Temperature (°C)")
axes[1].legend()
axes[1].grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(months, rainfall, color='blue', alpha=0.7, label="Rainfall (mm)")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall - Bar Chart")
plt.legend()
plt.grid(axis='y')
plt.show()

import numpy as np
plt.figure(figsize=(7, 7))
plt.pie(rainfall, labels=months, autopct='%1.1f%%', colors=plt.cm.Blues(np.linspace(0.3, 0.7, len(months))))
plt.title("Rainfall Distribution Across Months")
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# User input
months = list(map(int, input("Enter months (space-separated): ").split()))
rainfall = list(map(float, input("Enter rainfall (mm) (space-separated): ").split()))
temperature = list(map(float, input("Enter temperature (°C) (space-separated): ").split()))

x = np.arange(len(months))  # X-axis positions

fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2x2 grid for all plots

# 1. Line plot for rainfall & temperature
axes[0, 0].plot(months, rainfall, marker='o', linestyle='-', color='b', label="Rainfall (mm)")
axes[0, 0].plot(months, temperature, marker='s', linestyle='--', color='r', label="Temperature (°C)")
axes[0, 0].set_title("Rainfall & Temperature Trends")
axes[0, 0].set_xlabel("Months")
axes[0, 0].set_ylabel("Values")
axes[0, 0].legend()
axes[0, 0].grid(True)

# 2. Subplots in same row (Rainfall vs. Temperature separately)
axes[0, 1].plot(months, rainfall, marker='o', linestyle='-', color='b', label="Rainfall (mm)")
axes[0, 1].set_title("Monthly Rainfall")
axes[0, 1].set_xlabel("Months")
axes[0, 1].set_ylabel("Rainfall (mm)")
axes[0, 1].legend()
axes[0, 1].grid(True)

axes[1, 0].plot(months, temperature, marker='s', linestyle='--', color='r', label="Temperature (°C)")
axes[1, 0].set_title("Monthly Temperature")
axes[1, 0].set_xlabel("Months")
axes[1, 0].set_ylabel("Temperature (°C)")
axes[1, 0].legend()
axes[1, 0].grid(True)

# 3. Bar graph for rainfall & temperature
axes[1, 1].bar(x - 0.2, rainfall, width=0.4, color='b', label="Rainfall (mm)", alpha=0.7)
axes[1, 1].bar(x + 0.2, temperature, width=0.4, color='r', label="Temperature (°C)", alpha=0.7)
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(months)
axes[1, 1].set_title("Monthly Rainfall & Temperature")
axes[1, 1].set_xlabel("Months")
axes[1, 1].legend()
axes[1, 1].grid(axis='y')

plt.tight_layout()
plt.show()

# Pie chart for rainfall distribution
plt.figure(figsize=(7, 7))
plt.pie(rainfall, labels=months, autopct='%1.1f%%', colors=plt.cm.Blues(np.linspace(0.3, 0.7, len(months))))
plt.title("Rainfall Distribution Across Months")
plt.show()



