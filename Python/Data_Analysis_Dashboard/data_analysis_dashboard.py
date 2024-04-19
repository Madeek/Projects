import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Sample data
data = {
    
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [1000, 1200, 1500, 1800, 2000],
    'Expenses': [600, 700, 800, 900, 1000],
    'Profit': [400, 500, 700, 900, 1000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate additional metrics
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

# Print the DataFrame
print("Sample Data:")
print(df)

# Plotting with Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Sales'], marker='o', label='Sales')
plt.plot(df['Year'], df['Expenses'], marker='o', label='Expenses')
plt.plot(df['Year'], df['Profit'], marker='o', label='Profit')
plt.title('Sales, Expenses, and Profit Over Time')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.show()

# Plotting with Plotly
fig = px.bar(df, x='Year', y=['Sales', 'Expenses', 'Profit'], barmode='group', title='Sales, Expenses, and Profit Over Time')
fig.show()

# Plotting Profit Margin with Plotly
fig = px.line(df, x='Year', y='Profit Margin', title='Profit Margin Over Time')
fig.update_yaxes(title_text='Profit Margin (%)')
fig.show()
