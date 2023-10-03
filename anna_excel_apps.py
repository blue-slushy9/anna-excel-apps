import pandas as pd

# Load spreadsheet
xl = pd.ExcelFile(r'C:\users\blue-slushy9\desktop\Anna.xlsx')

# Load a sheet into a DataFrame by its name
df1 = xl.parse('Sheet1')

# Specify the columns you want to extract
columns = ['Application', 'Severity']  # replace with your column names

# Extract the specified columns and drop duplicates
df2 = df1[columns].drop_duplicates()

# THIS DIDN'T WORK, SAVING IT FOR INFORMATIONAL PURPOSES
# Print the data
# print(df2) >> 'C:\users\blue-slushy9\desktop\Anna.txt'

# Write the data to a text file
df2.to_csv('C:\\users\\blue-slushy9\\desktop\\Anna.txt', index=False)