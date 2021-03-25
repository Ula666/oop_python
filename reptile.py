# import Animal class
from animal import Animal

class Reptile(Animal): # we need to pass the animal class as an argument

    def __init__(self):
        super().__init__() # super is to make everything available from parent class
        self.cold_blooded = True
        self.tetrapod = None
        self.hart_chambers = [3,4]

    def hunt(self):
        return "working hard to catch the next meal"

    def use_venom(self):
        return "use it in danger"

    def seek_heat(self):
        return "looking for sunshine"

# benefits of inheritance
# reptile_object = Reptile()
#
# print(reptile_object.hunt())
# print(reptile_object.eat())
# print(reptile_object.move())

