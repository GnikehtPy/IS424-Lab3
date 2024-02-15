employees = {}

while True:
    name = input("Please enter employee name:\n")

    if name == "no":
        break

    try:
        salary = float(input("Please enter employee salary:\n"))
    except ValueError:
        print("Please enter a valid number")
        exit()

    employees[name] = salary

for employee in employees:
    print(f"Name: {employee}, Salary: {employees[employee]}")