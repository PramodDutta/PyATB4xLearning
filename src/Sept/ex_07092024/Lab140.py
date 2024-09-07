# Abstraction
# Abstraction - OOPs
# Hiding the details and showing the what is required

from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Pramod(Father):
    def loan(self):
        print("Paid the loan")

pramod = Pramod("1L")
pramod.loan()