from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__() # initialized everything from Snake class
        self.type = "python"

        self.large = True
        self.two_lungs = True

    def climb(self):
        return "up we go"

    def swallow(self):
        return "can't be bothered to chew"

python_object = Python()

print(python_object.move())  # from animal
print(python_object.climb()) # from this class