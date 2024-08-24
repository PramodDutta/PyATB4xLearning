# Leap Year Checker

year = int(input("Enter the year\n"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Lear Year")
