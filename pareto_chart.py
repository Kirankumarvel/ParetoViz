import matplotlib.pyplot as plt
import pandas as pd
import os
from utils.helpers import calculate_cumulative_percent

# Load data
data = pd.read_csv("data/sample_data.csv")

# Sort data
data = data.sort_values(by='Value', ascending=False)
categories = data['Category'].tolist()
values = data['Value'].tolist()

# Calculate cumulative %
cumulative_percent = calculate_cumulative_percent(values)

# Plot
fig, ax1 = plt.subplots()

# Bar chart
ax1.bar(categories, values, color="skyblue")
ax1.set_ylabel("Values", color="skyblue")
ax1.tick_params('y', colors='skyblue')

# Fix tick labels properly
ax1.set_xticks(range(len(categories)))
ax1.set_xticklabels(categories, rotation=45)

# Line chart
ax2 = ax1.twinx()
ax2.plot(range(len(categories)), cumulative_percent, color='red', marker='o')
ax2.set_ylabel('Cumulative %', color='red')
ax2.tick_params('y', colors='red')

# Title
plt.title('Pareto Chart Example')

# Save directory
os.makedirs("images", exist_ok=True)
plt.tight_layout()
plt.savefig("images/pareto_example.png")
plt.show()
