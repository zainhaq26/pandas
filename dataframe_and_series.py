#!/usr/bin/env python3

import pandas as pd

# df = pd.read_csv('employees.csv')

new_employees = {
    "EmployeeID": [51, 52, 53],
    "FirstName": ["Mike", "John", "Zain"],
    "LastName": ["Smith", "Doe", "Haq"],
    "Department": ["Marketing", "Sales", "Engineering"],
    "Position": ["Advertising", "Jr. Sales Rep", "Solutions Architect"],
    "Email": ["mike.smith@example.com", "joh.doe@example.com", "zain.haq@example.com"],
    "Phone": ["555-7890", "555-1234", "555-4321"],
    "HireDate": ["2024-11-14", "2024-10-17", "2024-12-30"],
    "Salary": ["90000", "50000", "150000"],
    "Location": ["San Francisco", "Atlanta", "New York"]
}

hire_date = new_employees["HireDate"]
# print(hire_date)

salary = new_employees["Salary"]
# print(salary)

df = pd.DataFrame(new_employees)

print(df.Email)
# prints out the column 'Email'

print(type(df["Email"]))
# prints <class 'pandas.core.series.Series'>
# A DataFrame is rows and columns (2 demensional). 
# A Series is rows of a single column (1 dimensional). 



