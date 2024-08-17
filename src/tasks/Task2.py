# Task #2: Mathematical Operations

# Get user inputs
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Perform calculations
maximum = max(num1, num2)
power = num1 ** num2
subtraction = num1 - num2
multiplication = num1 * num2
addition = num1 + num2
division = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"

# Print results using f-string formatting
print(f"\nResults:")
print(f"Maximum: {maximum}")
print(f"{num1} raised to the power of {num2}: {power}")
print(f"Subtraction (num1 - num2): {subtraction}")
print(f"Multiplication (num1 * num2): {multiplication}")
print(f"Addition (num1 + num2): {addition}")
print(f"Division (num1 / num2): {division}")