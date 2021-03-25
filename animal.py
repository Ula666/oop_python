# class is the keyword then name of the class
# Creating an Animal class
class Animal():

    # name = "Dog" # class variable
    def __init__(self): # self refers to the current class
        self.alive = True #attributes/ variables
        self.spine = True
        self.lungs = True

    def move(self):
        return "moving left right and forward"

    def eat(self):
        return "keep eating to stay alive"

    def breath(self):
        return "keep breathing to stay alive"

# creating an object of our Animal class
cat = Animal() # this will store all the data available
# in Animal class into cat
# print(cat.eat()) # eas() is now abstracted

# inheritance



   # pass # is a keyword used to bypass the code
