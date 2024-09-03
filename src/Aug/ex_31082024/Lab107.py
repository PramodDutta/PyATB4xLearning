class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    def talk(self):  # NRNG  # self - this , self will be first argument in every behaviour.
        print("I can talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):  # No Arg with Return
        return "I am walking"


# Create an Object of the Class
# ObjectRef = ClassName() -> Object
tushar = Person()
tushar.name = "tushar"
print(tushar.name)
tushar.talk()


rajyalakshmi = Person()
rajyalakshmi.name = "rajyalakshmi"
print(rajyalakshmi.name)
rajyalakshmi.talk() 

