# def sum_three_num(a,b,c):
#     return a+b+c


# op = lambda a, b, c: a + b + c
# print(op(322, 32, 21121))


def find_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# find_odd_even(5)

check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(11))
