import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('C:\\Users\\Ajay Kumar Kalra\\Desktop\\data.csv')

# Analysis 1: Product-wise Total Net Sales
product_wise_sales = df.groupby('Product Type')['Total Net Sales'].sum().sort_values(ascending=False)
print("\nProduct-wise Total Net Sales:\n", product_wise_sales)

# Visualization 1: Bar chart for Product-wise Total Net Sales
plt.figure(figsize=(12, 6))
sns.barplot(x=product_wise_sales.index, y=product_wise_sales.values)
plt.title('Product-wise Total Net Sales')
plt.xlabel('Product Type')
plt.ylabel('Total Net Sales')
plt.xticks(rotation=45, ha='right')
plt.show()

# Analysis 2: Correlation between variables
#correlation_matrix = df.corr()
#print("\nCorrelation Matrix:\n", correlation_matrix)

# Visualization 2: Heatmap for Correlation Matrix
plt.figure(figsize=(10, 8))
#sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Analysis 3: Sales Trends Over Time
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])
df['Month'] = df['PurchaseDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total Net Sales'].sum()

# Visualization 3: Line chart for Sales Trends Over Time
plt.figure(figsize=(12, 6))
monthly_sales.plot(marker='o', color='b')
plt.title('Sales Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Total Net Sales')
plt.xticks(rotation=45, ha='right')
plt.show()
