# OOPs
# Class - Blueprint
# OBject - Instance of class
# Encapsulation - private __, protected _, public.
# Inheritance - single, multiple, multilevel, heri, hybrid
# Poly - method overriding, method overloading(x)
# self, super, __init__

# Abstraction
# Hide the details and show what is required.

# Car - with key _ __private, tyres -> public,

# Car -> multiple - Engine, GearBox
# Car -> driver -> Engine, gearbox?
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Bark")


dog = Dog("PP")
dog.sound()
