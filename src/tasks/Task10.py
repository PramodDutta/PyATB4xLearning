# FACTORIAL

#n = 0 or 1 -> FACT 1=
#N 5 -> 5*4*3*2*1 = 120

num = int(input("Enter the int number")) # 5
fact = 1
if num == 0 or num == 1:
    fact = 1
    print(1)
else:
    for i in range(1, num + 1,1): # 1, 5
        fact = fact*i

    # i = 1
    # while(i<= num):
    #     fact = fact*i
    #     i = i+1

    # | i  |  o/p |  fact |
    # | 1  |  NA |  fact  = 1* 1 | fact =1
    # | 2  |  NA |  fact  = 1* 2 | fact =2
    # | 3  |  NA |  fact  = 2* 3 | fact =6
    # | 4  |  NA |  fact  = 6* 4 | fact =24
    # | 4  |  NA |  fact  = 24* 5 | fact =120

print(fact) # 120

