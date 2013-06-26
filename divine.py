#!/usr/bin/env python2
#######################       N
#       DIVINE        #     W   E
#                     #       S
# u_l     u_m     u_r #
# A##     B##     C## #
# ###     ###     ### #
# ###     ###     ### #
#                     #
# m_l     m_m     m_r #
# D##     E##     F## #
# ###     ###     ### #
# ###     ###     ### #
#                     #
# b_l     b_m     b_r #
# G##     H##     I## #
# ###     ###     ### #
# ###     ###     ### #
#                     #
#        enter        #
#######################

import random, sys, collections

TREASURE_X = random.randrange(0, 2)
TREASURE_Y = random.randrange(0, 2)
X_MIN = 0
X_MAX = 2
Y_MIN = 0
Y_MAX = 2

class Room:
    def __init__(self, x, y):
        if x < X_MIN or x > X_MAX:
            raise Exception("Invalid x coordinate.")
        else:
            self.x = x

        if y < Y_MIN or y > Y_MAX:
            raise Exception("Invalid y coordinate.")
        else:
            self.y = y

    def getDirections(self):
        """ Prints all possible directions to move in. """
        dirs = []

        if self.x == X_MIN:
            dirs.append("east")
        elif self.x == X_MIN + 1:
            dirs.append("east")
            dirs.append("west")
        else:
            dirs.append("west")

        if self.y == Y_MIN:
            dirs.append("north")
        elif self.y == Y_MIN + 1:
            dirs.append("north")
            dirs.append("south")
        else:
            dirs.append("south")

        return dirs

class Occupant:
    def __init__(self):
        self.location = Room(random.randrange(0, 2), random.randrange(0, 2))

    def getLocation(self):
        names = [ ["The Solar", "The Mezzanine", "The Lords & Ladies Chamber"],
                  ["The Bower", "The Great Hall", "The Bottlery"],
                  ["The Chapel", "The Oratory", "The Bailey"],
                ]
        return names[self.location.x][self.location.y]

def move(Occupant):
    """ Move occupant based off direction.
    Should also print the current room location.
    """

    print "You are currently at: " + Occupant.getLocation()
    print "Which direction would you like to go?"
    dirs = Occupant.location.getDirections()
    for i in dirs:
        print "\t" + i

    checkdirs = set(dirs)
    direction = raw_input("> ")

    if direction in checkdirs:
        if direction == "east":
            Occupant.location.x += 1
        elif direction == "west":
            Occupant.location.x -= 1
        elif direction == "north":
            Occupant.location.y += 1
        else:
            Occupant.location.y -= 1
        print "You are now here: " + Occupant.getLocation()
    else:
        move(Occupant)

def checkTreasure(Occupant):
    """ Determines if you have won the game or not. """
    if Occupant.location.x == TREASURE_X and Occupant.location.y == TREASURE_Y:
        win()

def win(Occupant):
    print "You have found the treasure in %s!" % Occupant.getLocation()
    sys.exit()

if __name__ == '__main__':
    robin = Occupant()
    move(robin)
    room = Room(0, 1)
    room.getDirections()
    #print """You awake as a thief in search of gold in front of Divine, a mystical castle.
    #You believe the treasure is here; however, you may choose to enter or leave.
    #"""
    #robin = Occupant()
    #move(robin)
