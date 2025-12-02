# Task 1 - Employee Record System
# Console-based program to store and display employee details using OOP.

class Employee:

    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee Name : {self.name} || Employee ID : {self.emp_id}")
        print(f"Department : {self.department} || Salary : {self.salary}")


class EmployeeRecordSystem:
    def __init__(self):
        self.employees = []  # store employee objects

    def add_employee(self):
        print("\n--- Add Employee Details ---")
        name = input("Enter Employee Name : ")
        emp_id = input("Enter Employee ID : ")
        department = input("Enter Department : ")
        salary = input("Enter Salary($): ")

        employee = Employee(name, emp_id, department, salary)
        self.employees.append(employee)
        print("\nEmployee Added Successfully!")

    def display_employees(self):
        print("\n--- Employee Records ---")
        if not self.employees:
            print("No employee data available.")
        else:
            for emp in self.employees:
                emp.display_employee_info()

def main():
    system = EmployeeRecordSystem()

    while True:
        print("\n===== Employee Record System =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            system.add_employee()
        elif choice == "2":
            system.display_employees()
        elif choice == "3":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

# Start Program
main()