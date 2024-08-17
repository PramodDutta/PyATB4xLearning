# Task #1: Multiplication Table

# Get user input
num = int(input("Enter a number to print its multiplication table: "))

# Print the multiplication table
print(f"Multiplication Table for {num}:\n")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")