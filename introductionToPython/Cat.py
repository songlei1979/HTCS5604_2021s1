from introductionToPython.Feline import Feline


class Cat(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.call = "miaow"

feline = Feline()
print(feline.leg)

cat = Cat()
print(cat.leg)
print(cat.call)
