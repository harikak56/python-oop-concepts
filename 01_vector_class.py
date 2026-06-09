# ============================================
# Topic   : Magic Methods (Operator Overloading)
# Question: Create a Vector class that supports
#           + and * operators using magic methods
# ============================================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 1)

print(v1 + v2)  # Output: Vector(6, 4)
print(v1 * 3)   # Output: Vector(6, 9) 
