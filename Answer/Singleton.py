#   Singleton
# It’s a design pattern that ensures a class has only one object (instance) throughout the app — like a single log manager
#
# Only one object of a class is ever created, no matter how many times you try to make it.
#  	Saving memory, shared global state

class Singleton:
     # stores the single instance
    _instance = None  
    
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # create new instance
        return cls._instance

# Testing
a = Singleton()
b = Singleton()

print(a is b)  # ✅ Output: True (both are same instance)

# __new__ is a special method that creates a new object.

# We override it to check if an instance already exists.

# If yes, return the same one instead of creating a new one
