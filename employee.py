class Employee:
    def __init__(self, id, name, designation) -> None:
        self.id = id
        self.name = name
        self.designation = designation


p1 = Employee(1,"Hari","Engineer")

print(p1.name)
print(p1.designation)