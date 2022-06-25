class Employee:
    def __init__(self, name, designation, salary) -> None:
        self.name = name
        self.designation = designation
        self.salary = salary


p1 = Employee("Hari","Engineer",10000)

print(p1.name)
print(p1.designation)
print(p1.salary)