# Web Automation - Selenium
# Page - You are going automate


class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg
        # self.name = name
        # self.last_name = last_name

    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed to Login")
        else:
            print("Not allowed")


# This is the end of the class

email = input("Enter the email \n")
password = input("Enter the password \n")

vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()


pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
pramod.login_confirm()
