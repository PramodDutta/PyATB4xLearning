# Functions Scope
pb_global_b = 12 # almost work like a global varibale
def my_function():
    pb_a = 10 # local variable, within the function
    print(pb_a)
    print(pb_global_b)

def f1():
    print(pb_global_b)

# print(pb_a)
my_function()
print(pb_global_b)
f1()