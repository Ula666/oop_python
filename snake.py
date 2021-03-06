# import reptile class
from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = True
        self.fork_tongue = True


    def use_tongue_to_smell(self):
        return "use tongue to smell the food"

    def shed_skin(self):
        return "growing shed skin"

snake_object = Snake()

# print(snake_object.eat())  # eat() is inherited from the Animal class
# print(snake_object.move())  # move() from Animal class
# print(snake_object.hunt())  # hunt() is inherited from Reptile class
# print(snake_object.use_tongue_to_smell())  #from current class
#multiple inheritance