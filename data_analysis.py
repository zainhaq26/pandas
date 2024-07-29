#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('employees.csv')

# returns first 5 rows. Pass in a value to see more rows, ie df.head(10)
# df.head()

# returns last 5 rows. Pass in a value to see more rows, ie df.tail(10)
# df.tail()

# Returns the column FirstName
first_name = df['FirstName']
# print(first_name)

# Returns the columns Email`` and Phone
email_phone = df[['Email', 'Phone']]
# print(email_phone)

# returns all employees in the engineering Department
engineering = df[(df['Department'] == 'Engineering')]
# print(engineering)

# creates a new csv file with all employees in the engineering Department
# engineering.to_csv('engineering_department.csv') 

# gives the number of rows and columns from parsed data
rows_and_colums = df.shape
# print(rows_and_colums)

# Get all the columns and the dataypes for each column
# data_type = df.info()

pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 3)

# Gives schema. Column information. What each column data represents.
schema_df = pd.read_csv('employees.csv')
print(schema_df)