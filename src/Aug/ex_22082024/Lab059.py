# Match Statement
# Switch in Java
# match the op and execute
# Python > 3.10

# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block

# Write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name == "firefox":
            print("Hello Hello")
        print("Excute the firefox Code")
    case "chrome":
        print("Excute the Chrome Code")
    case "edge":
        print("Excute the Edge Code")
    case "safari":
        print("Excute the Safari Code")
    case _:
        print("Browser Not Found!")

