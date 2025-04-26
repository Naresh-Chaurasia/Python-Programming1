# This is the decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # original function
        print("Something is happening after the function is called.")
    return wrapper

# This is the function we want to decorate
@my_decorator
def say_hello():
    print("Hello!")

# Calling the function
say_hello()
