# ============================================
# Topic   : Class Variables
# Question: Create a class Employee where every
#           time a new instance is created, a
#           class-level variable total_employees
#           increments.
# ============================================

class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1


e1 = Employee("Harika")
e2 = Employee("Ravi")
e3 = Employee("Priya")

print(e1.name)                              # Output: Harika
print(Employee.total_employees)             # Output: 3
