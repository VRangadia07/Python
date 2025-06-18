# A decorator in Python is a powerful tool that allows 
# you to modify or enhance the behavior of functions or classes
# without changing their code.

# A decorator is essentially a function that takes another
# function as input, adds some functionality, and returns a 
# new function.

def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# def make_pretty(func):
#     # define the inner function 
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")

#         # call original function
#         func()
#     # return the inner function
#     return inner

# # define ordinary function
# def ordinary():
#     print("I am ordinary")
    
# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)

# # call the decorated function
# decorated_func()

def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  

# decortae kare 6e ke le6e ek bija function as argu. and some add funcationlity and give to modifly new version.