user_type = input("Enter the user type, admin, manager, guest\n")
user_type = user_type.lower()
match user_type:
    case "admin" | "manager":
        print("Hello Sir")
    case "guest":
        print("Hello, Guest")
    case _:
        print("Hello, There!")
