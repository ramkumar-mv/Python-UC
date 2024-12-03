# Author: Ramkumar M V
# GitHub: https://github.com/ramkumar-mv/Python-UC

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#ingesting data from a CSV file
data = pd.read_csv('data.csv')

print("Initial Data:")
print(data.head())

#managing different data types
data['date'] = pd.to_datetime(data['date'])
data['category'] = data['category'].astype('category')
data['value'] = pd.to_numeric(data['value'], errors='coerce') 
data['value'].fillna(data['value'].mean(), inplace=True)


#wrangling the data using filtering and grouping
filtered_data = data[data['value'] > 10]
grouped_data = filtered_data.groupby('category').sum()

#custom function for analysis which returns the description of the dataset
def analyse_data(df):
    return df.describe()

#using a function for data analysis
analysis_result = analyse_data(grouped_data)
print("\nAnalysis Result:")

#printing the analysis result
print(analysis_result)

#visualizing the data using matplotlib - bar chart
plt.figure(figsize=(12, 6))
plt.bar(grouped_data.index, grouped_data['value'], color='skyblue')
plt.title('Total Value by Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Total Value', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('bar_chart.png') 
plt.show()

#visualizing the data using matplotlib - pie chart
plt.figure(figsize=(8, 8))
plt.pie(grouped_data['value'], labels=grouped_data.index, autopct='%1.1f%%', startangle=140)
plt.title('Category Distribution', fontsize=16)
plt.axis('equal')  
plt.savefig('pie_chart.png')
plt.show()

#saving the analysis result in text file for record-keeping
with open('analysis_result.txt', 'w') as f:
    f.write(str(analysis_result))