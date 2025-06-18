# Method Resolution Order (MRO) in Python
# If two superclasses have the same method (function) name and the derived class calls that method, Python uses the MRO to search for the right method to call. For example,

class SuperClass1:
    def info(self):
        print("Super Class 1 method called")

class SuperClass2:
    def info(self):
        print("Super Class 2 method called")

class Derived(SuperClass1, SuperClass2):
    pass

d1 = Derived()
d1.info()  

# Output: "Super Class 1 method called"
# Run Code
# Here, SuperClass1 and SuperClass2 both of these classes define a method info().

# So when info() is called using the d1 object of the Derived class, Python uses the MRO to determine which method to call.

# In this case, the MRO specifies that methods should be inherited from the leftmost superclass first, so info() of SuperClass1 is called rather than that of SuperClass2.