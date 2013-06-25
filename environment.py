import random

TREASURE = random.randrange(1, 9)

class Room:
    def __init__(self, location):
        if location == "upperLeft":
            self.number = 1
            self.dirs = ["east" , "south"]
        elif location == "upperMid":
            self.number = 2
            self.dirs = ["east", "south", "west"]
        elif location == "upperRight":
            self.number = 3
            self.dirs = ["south", "west"]
        elif location == "midLeft":
            self.number = 4
            self.dirs = ["north", "east", "south"]
        elif location == "midMid":
            self.number = 5
            self.dirs = ["north", "east", "south", "west"]
        elif location == "midRight":
            self.number = 6
            self.dirs = ["south", "west", "east"]
        elif location == "bottomLeft":
            self.number = 7
            self.dirs = ["north", "east"]
        elif location == "bottomMid":
            self.number = 8
            self.dirs = ["north", "east", "west"]
        elif location == "bottomRight":
            self.number = 8
            self.dirs = ["north", "east"]
        else:
            raise Exception("Invalid room location.")

    def getTreasure(self):
        """ Returns whether or not the room holds treasure. """
        return self.number == TREASURE

    def getDirections(self):
        """ Prints all possible directions to move in. """
        for directions in self.dirs:
            print directions
