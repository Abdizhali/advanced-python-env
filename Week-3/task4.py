class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_role(self):
        return "Employee"

    def get_salary(self):
        return self._salary

class Manager(Employee):
    def get_role(self):
        return "Manager"

def show(employees):
    for e in employees:
        print(e.get_role(), e.get_salary())

show([Employee(500), Manager(1000)])
