# creating the employee class using multiple inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person initialized: {self.name}, {self.age}")

class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department
        print(f"Employee initialized: {self.employee_id}, {self.department}")

class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department, title):
        # Initialize base classes
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, department)
        # Initialize the Manager specific attributes
        self.title = title
        print(f"Manager initialized: {self.title}")

# Create an instance of Manager
manager = Manager("Alice", 35, "E123", "HR", "Senior Manager")
