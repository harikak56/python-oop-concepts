# ============================================
# Topic   : Multiple Inheritance & MRO
# Question: Create Flyer, Swimmer, and Duck class.
#           Duck inherits from both. Show how
#           Python decides which move() to call.
# ============================================

class Flyer:
    def move(self):
        return "Flying!"

class Swimmer:
    def move(self):
        return "Swimming!"

class Duck(Flyer, Swimmer):
    pass


d = Duck()
print(d.move())         # Output: Flying!

# Python checks left to right: Duck → Flyer → Swimmer
print(Duck.__mro__)     # Output: (<class 'Duck'>, <class 'Flyer'>, <class 'Swimmer'>, <class 'object'>)
