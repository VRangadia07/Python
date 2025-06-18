# Abstraction means hiding the unnecessary details and showing 
# only the important parts to the user.
# 
# Abstraction is used in Object-Oriented Programming (OOP) to 
# hide complex code and only show the essential features.

# Python does this using abstract classes and methods 
# (via the abc module).



from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

# Subclass must define the abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")

# Can't create an object of Vehicle (it's abstract)
# v = Vehicle()  #  Error

# But you can create an object of Car
my_car = Car()
my_car.start_engine()  # Output: Car engine started!

#  interface

# Python doesn’t have a built-in interface keyword like Java or C#,
# but we use abstract classes with only abstract methods to act like interfaces.


from abc import ABC, abstractmethod

# This is an interface
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Classes must follow the "Animal" interface
class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Using the interface
def animal_sound(animal: Animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow

