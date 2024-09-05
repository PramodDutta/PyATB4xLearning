class Grandparent:
    key_gold ="1kg"
    def grandparent_method(self):
        return "Grandparent's method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    mac_m3_apple = "M3 Max"
    def child_method(self):
        return "Child's method"

child = Child()
print(child.grandparent_method())