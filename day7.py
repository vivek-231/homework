import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('sales_data.csv')

# Display the first 5 rows of the dataset
print(df.head())
# Assuming there's a 'Region' column and a 'Sales' column in the dataset
total_sales_region = df.groupby('Region')['Sales'].sum()
print(total_sales_region)
# Assuming there are 'Profit' and 'Sales' columns
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

# Compute the average profit margin for each product
avg_profit_margin = df.groupby('Product')['Profit Margin'].mean()
print(avg_profit_margin)
