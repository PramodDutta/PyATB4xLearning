# User Defined
# 1. The can't return -> non return
# 2.They can return something
# They have parameters
# They don't parameters / arguments


# 1. The can't return -> non return
# # No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello World")


result = greet()
print(result)


# 2. # No Return Type and with Argument
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Pramod")


# # 3. No Return Type and with Default Argument
def say_hello_default_arg(name="pramod"):
    print("Hello", name.upper())


say_hello_default_arg("Amit")
say_hello_default_arg()
say_hello_default_arg(name="Tushar")  # positional argument


def multiple_args(name1="Arpita", name2="Pramod", name3="Amit"):
    print("Multiple Arguments", name1, name2, name3)


multiple_args(name1="Ram", name2="Yunus", name3="Deepshikha")
multiple_args(name1="PRAMOD")


# 4. Argument + return Type
def sum_of_two_number(num1, num2):
    return num1 + num2


def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2


# result = sum_of_two_number(10, 34)
result = sum_of_two_number(num1=34, num2=34)
result = sum_of_two_number_with_default()
print(result)
