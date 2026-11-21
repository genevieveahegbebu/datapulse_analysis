# ── IMPORTS (always at the top) ──────────────────────────────────────────
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# ── LOAD DATA ────────────────────────────────────────────────────────────
# pd.read_csv() reads a CSV file and returns a DataFrame (a table in Python)
# The file must be in the same folder as this script, or provide a full path
df = pd.read_csv('sales_data.csv')
 
# ── INSPECT THE DATA ─────────────────────────────────────────────────────
# .shape returns (number of rows, number of columns) as a tuple
print(f'Shape: {df.shape[0]} rows, {df.shape[1]} columns')
 
# .head(n) prints the first n rows — default is 5
print(df.head())
 
# .dtypes shows the data type Python assigned to each column
print(df.dtypes)
 
# .describe() prints count, mean, std, min, quartiles, max for numeric columns
print(df.describe())
 
# ── COMPUTE WITH NUMPY ───────────────────────────────────────────────────
# Extract the revenue column as a Python list, then use numpy for statistics
revenue = df['revenue'].tolist()
print(f'Mean revenue  : GHS {np.mean(revenue):,.2f}')
print(f'Total revenue : GHS {np.sum(revenue):,.2f}')
print(f'Highest day   : GHS {np.max(revenue):,.2f}')
 
# ── VISUALISE WITH MATPLOTLIB ────────────────────────────────────────────
# plt.figure() sets the chart size in inches
# plt.plot() draws a line chart | plt.show() renders and displays it
plt.figure(figsize=(10, 4))
plt.plot(df['date'], df['revenue'], color='steelblue', linewidth=2)
plt.title('Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue (GHS)')
plt.tight_layout()   # prevents labels from being cut off
plt.show()