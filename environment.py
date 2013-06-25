import random
import sys

TREASURE = random.randrange(1, 9)

class Room:
    def __init__(self, location):
        if location == "upperLeft":
            self.number = 1
            self.dirs = {"east": "upperMid", "south": "midLeft"}
        elif location == "upperMid":
            self.number = 2
            self.dirs = {"east": "midMid", "south": "botMid", "west": "upperLeft"}
        elif location == "upperRight":
            self.number = 3
            self.dirs = {"south": "midRight"  , "west": "midMid"}
        elif location == "midLeft":
            self.number = 4
            self.dirs = {"north": "upperLeft", "east": "midMid", "south": "botLeft"}
        elif location == "midMid":
            self.number = 5
            self.dirs = {"north": "upperMid", "east": "midLeft", "south": "botMid", "west": "midLeft"}
        elif location == "midRight":
            self.number = 6
            self.dirs = {"south", "west", "east"}
        elif location == "botLeft":
            self.number = 7
            self.dirs = {"north", "east"}
        elif location == "botMid":
            self.number = 8
            self.dirs = {"north": "midMid", "east": "botRight", "west": "botLeft"}
        elif location == "botRight":
            self.number = 9
            self.dirs = {"north": "midRight", "east": "botMid"}
        else:
            raise Exception("Invalid room location.")


    def getDirections(self):
        """ Prints all possible directions to move in. """

        for directions in self.dirs:
            print "\t" + directions


class Occupant:
    def __init__(self):
        self.location = Room("botMid")

    def getLocation(self):
        chambers = {
                    1: "Upper Left Chamber",
                    2: "Upper Middle Chamber",
                    3: "Upper Right Chamber",
                    4: "Middle Left Chamber",
                    5: "Middle Middle Chamber",
                    6: "Middle Right Chamber",
                    7: "Bottom Left Chamber",
                    8: "Bottom Middle Chamber",
                    9: "Bottom Right Chamber",
        }
        return chambers[self.location.number]

    # This function needs to be in divine.py because I will initialize all room
    # objects as variables and just have the occupant move to those variables.
    def move(self):
        """ Move occupant based off direction.
        Should also print the current room location.
        """

        print "You are currently in: " + self.getLocation()
        print "Which direction would you like to go?"

        dirs = set(self.location.dirs)
        self.location.getDirections()
        direction = raw_input("> ")

        if direction in dirs:
            self.location = Room(self.location.dirs[direction])
        else:
            self.move()

robin = Occupant()
robin.move()
