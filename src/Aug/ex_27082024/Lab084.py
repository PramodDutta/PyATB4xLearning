# @staticmethod
# @classmethod
# @property
# @functools.wraps
# These we will use them int the OOPs


# Chaining Decorators

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")
    
say_hello()

