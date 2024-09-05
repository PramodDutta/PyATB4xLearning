class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")


class Child(Parent):
    diamond = "Diamond"
    def BHK3(self):
        print("3BHK")


child_object= Child()
print(child_object.gold)
child_object.BHK3()
child_object.BHK2()

father_obect_ref = Parent()
father_obect_ref.BHK2()
# father_obect_ref.BHK3() # AttributeError: 'Parent' object has no attribute 'BHK3'. Did you mean: 'BHK2'?
# print(father_obect_ref.diamond)





