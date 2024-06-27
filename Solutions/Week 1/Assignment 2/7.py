salary = float(input("Enter the salary = "))
if salary < 10000:
    increment = 0.05
elif salary <= 20000:
    increment = 0.10
elif salary <= 50000:
    increment = 0.15
else:
    increment = 0.20

updated_salary = salary + (salary * increment)
print(f"Updated salary = {updated_salary}")
