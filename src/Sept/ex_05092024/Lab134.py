class GF:
    def car(self):
        return "Old car"

class F(GF):
    pass
    # def car(self):
    #     return "honda civic"

class S(F):
    pass
    # def car(self):
    #     return "Lambo"

son = S()
print(son.car())
