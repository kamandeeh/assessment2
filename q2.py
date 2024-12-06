class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = [] 

    def add_employees(self, employee):
        self.employees.append(employee)

    def remove_employees(self, employee):
        self.employees.remove(employee)


employee1 = Employee("Zuruel", 12345678)
employee2 = Employee("James", 87654321)


department = Department("IT Department")

# Add employees to the department
department.add_employees(employee1) 
department.add_employees(employee2)  

# Print employee names in the department
for employee in department.employees:
    print(f"Employee Name: {employee.name}, Employee ID: {employee.id}")
