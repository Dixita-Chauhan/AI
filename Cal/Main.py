# Ekdam simple Dictionary data store karne ke liye
employee_database = {}

print(" Welcome to Employee Management System ")

# 1. User se data input lena
emp_name = input("Enter employee name: ")
emp_salary = input("Enter employee salary: ")
emp_role = input("Enter employee  role(e.g., Developer, Manager): ")

# 2. Data ko database (Dictionary) me save karna
employee_database["Name"] = emp_name
employee_database["Salary"] = emp_salary
employee_database["Role"] = emp_role

# 3. Data ko screen par professional tarike se print karna
print("\n====================================")
print("EMPLOYEE PROFILE CREATED SUCCESSFULLY")
print("====================================")
print(f" Name   : {employee_database['Name']}")
print(f"Role   : {employee_database['Role']}")
print(f" Salary : ₹{employee_database['Salary']}/month")
print("====================================")
