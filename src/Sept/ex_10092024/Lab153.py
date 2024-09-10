# try, except and finally

try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1/num2
except ValueError as ve:
    print("Value Error, You have entered the string instead we want int")
except ZeroDivisionError as zde:
    print("Zero Div error, Don't use the Num2 as 0")
else:
    print(f"Result is {result}")
finally:
    print("This code will be always executed.!")