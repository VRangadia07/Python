# @property 
# Acts like an attribute, but it runs a method behind the scenes.
# Turns a method into a read-only attribute.Allows you to access a method without calling it with ().

# Often used to encapsulate private variables and apply logic when getting values.

class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
        p = Person("Alice")
        print(p.name) # Get name
        p.name = "Bob" # Set name
    
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

t = Temperature(0)
print(t.fahrenheit)  # Output: 32.0



# classmethod Works on the class itself, not an instance.
# A method bound to the class, not the instance.Takes cls as the first parameter, representing the class itself

# When the method needs to work with class-level data (like modifying a class variable).

class Person:
    population = 0  # class variable

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

# Usage
p1 = Person("Alice")
p2 = Person("Bob")

print(Person.get_population())  # Output: 2

# get_population() can be called without creating an object and cls allows you to work with the class itself.



# @staticmethod
# A method that doesn’t access class or instance data.No self or cls parameter.

# A regular function, just placed inside a class for organization

class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

# Usage
print(Math.multiply(4, 5))  # Output: 20

# It keeps related functionality inside the class.

# But it doesn’t require access to the class or object data.

