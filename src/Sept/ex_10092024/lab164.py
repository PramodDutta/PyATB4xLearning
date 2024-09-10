with open("TestData.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line,end="")