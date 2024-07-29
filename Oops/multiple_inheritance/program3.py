# multiple inheritance for employee method

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
        super().__init__(name, age)  # This will call Person's __init__
        Employee.__init__(self, employee_id, department)  # Explicit call to Employee's __init__
        self.title = title
        print(f"Manager initialized: {self.title}")

manager = Manager("Alice", 35, "E123", "HR", "Senior Manager")
