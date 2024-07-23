import pandas as pd

df = pd.read_csv('employees.csv')

# Returns the column FirstName
first_name = df['FirstName']
# print(first_name)

# Returns the columns Email and Phone
email_phone = df[['Email', 'Phone']]
# print(email_phone)

# returns all employees in the engineering Department
engineering = df[(df['Department'] == 'Engineering')]
# print(engineering)

# creates a new csv file with all employees in the engineering Department
# engineering.to_csv('engineering_department.csv') 
