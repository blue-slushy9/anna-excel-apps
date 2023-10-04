# Had to install Openpyxl in the Terminal, which is a Python library for
# working with Excel spreadsheets;

# Pandas is a library for data manipulation and analysis, it is often used by
# data scientists;
import pandas as pd

# Load spreadsheet; the 'r' means the following string should be interpreted
# in raw format, i.e. as a string literal;
xl = pd.ExcelFile(r'C:\users\blue-slushy9\desktop\Anna.xlsx')

# Load a sheet into a DataFrame by its name; a DataFrame is a two-dimensional
# data structure in Pandas/Openpyxl, used to store and manipulate different 
# data types; parse() method extracts information per following instructions;
df1 = xl.parse('Sheet1')

# Specify the columns you want to extract;
columns = ['Application', 'Severity']

# Extract the specified columns and drop (forget) duplicates;
df2 = df1[columns].drop_duplicates()

# Write the data to a text file; we use the '\\' because in Python the '\' is
# an escape character; this tells Python we actually want backslashes;
df2.to_csv('C:\\users\\blue-slushy9\\desktop\\Anna.txt', index=False)