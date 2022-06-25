class Employee:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation


p1 = Employee("Hari","Engineer")

print(p1.name)
print(p1.designation)