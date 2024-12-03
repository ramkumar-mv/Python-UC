# Author: Ramkumar M V
# GitHub: https://github.com/ramkumar-mv/Python-UC

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#ingesting data from a CSV file
data = pd.read_csv('data.csv')

#managing different data types
data['date'] = pd.to_datetime(data['date'])
data['category'] = data['category'].astype('category')

#wrangling the data using filtering and grouping
filtered_data = data[data['value'] > 10]
grouped_data = filtered_data.groupby('category').sum()

#custom function for analysis which returns the description of the dataset
def analyse_data(df):
    return df.describe()

#using a function for data analysis
analysis_result = analyse_data(grouped_data)

#visualizing the data using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(grouped_data.index, grouped_data['value'], color='blue')
plt.title('Value by Category')
plt.xlabel('Category')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#printing the analysis result
print(analysis_result)