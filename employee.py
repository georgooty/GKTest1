class Employee:
<<<<<<< HEAD
    def __init__(self, name, designation, salary) -> None:
=======
    def __init__(self, id, name, designation) -> None:
        self.id = id
>>>>>>> c89d95a4384d37d05fce72a3838e107af5a7179d
        self.name = name
        self.designation = designation
        self.salary = salary


<<<<<<< HEAD
p1 = Employee("Hari","Engineer",10000)
=======
p1 = Employee(1,"Hari","Engineer")
>>>>>>> c89d95a4384d37d05fce72a3838e107af5a7179d

print(p1.name)
print(p1.designation)
print(p1.salary)