# Continue Statement
# continue statement skips the current iteration of a loop and
# moves to the next iteration.

for number in range(10):
    if number % 2 == 0:
        continue
    else:
        print(number)

# | i  | Condition | O/P
# | 0  | 0%2 == 0 -> True | continue - skip No O/P
# | 1  | 1%2 == 0 -> False | 1
# | 2  | 1%2 == 0 -> True | continue - skip No O/P
# | 3  | 3%2 == 0 -> False | 3


# pass - can be used in the statment, fucntions, class and obejcts