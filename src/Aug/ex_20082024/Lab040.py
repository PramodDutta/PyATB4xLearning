# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .

# Logic ?  If else - 1 condition
# more 1 condition -> if elif else

# Syntax
# if condition 1:
#     print("do 1")
# elif condition 2:
#     print("do 2")
# elif condition 3:
#     print("do 4")
# else:
#     print(" do 4")


num1 = int(input("Enter the num1\n"))  # 5 , # 10
num2 = int(input("Enter the num2\n"))  # 3 , # 12
num3 = int(input("Enter the num3\n"))  # 2 , # 11

#  5 > 3 and 5 > 2 -> true -> 5
# num 1 >  num2  and num 1 > num 3 ->  num 1

#  12 > 10 and 12 > 11 -> true -> 12
# num 2 >  num1  and num 2 > num 3 ->  num 2

# num 3

if num1 > num2 and num1 > num3:
    print("Max is ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is ", num2)
else:
    print("Max is ", num3)

result = max(num1, num2, num3)
print(result)
