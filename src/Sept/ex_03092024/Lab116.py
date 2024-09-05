a = 10


class Person:
    b = 11 # Instance - Belong to class
    c = 11 # Instance - Belong to class

    def print_infor(self):
        global a # Declare it as global
        a = "Hello"
        print(self.b)
        print(self.c)



object_Ref = Person()
object_Ref.print_infor()
print(a)
# print(b)
