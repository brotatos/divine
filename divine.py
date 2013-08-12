#!/usr/bin/env python2
# Copyright (c) 2012-2013 Robin Choudhury
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#######################       N
#       DIVINE        #     W   E
#                     #       S
# ###     ###     ### #
# ###     ###     ### #
# ###     ###     ### #
#                     #
# ###     ###     ### #
# ###     ###     ### #
# ###     ###     ### #
#                     #
# ###     ###     ### #
# ###     ###     ### #
# ###     ###     ### #
#                     #
#######################

from random import randrange
from sys import exit

TREASURE_X = randrange(0, 2)
TREASURE_Y = randrange(0, 2)
X_MIN = 0
X_MAX = 2
Y_MIN = 0
Y_MAX = 2


class Room(object):

    def __init__(self, x, y):
        if x < X_MIN or x > X_MAX:
            raise Exception("Invalid x coordinate.")
        else:
            self.x = x

        if y < Y_MIN or y > Y_MAX:
            raise Exception("Invalid y coordinate.")
        else:
            self.y = y

    def get_directions(self):
        """Prints all possible directions to move in."""
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


class Occupant(object):

    def __init__(self):
        self.location = Room(randrange(0, 2), randrange(0, 2))

    def get_location(self):
        """Assigns room names to rooms based of cartesian coordinates."""
        names = [["The Solar", "The Mezzanine", "The Lords & Ladies Chamber"],
                 ["The Bower", "The Great Hall", "The Bottlery"],
                 ["The Chapel", "The Oratory", "The Bailey"]
                 ]
        return names[self.location.x][self.location.y]


def move(Occupant):
    """Move occupant based off direction. Print the current room location."""

    print "\nYou are currently at: " + Occupant.get_location()
    print "Which direction would you like to go?"
    dirs = Occupant.location.get_directions()
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
        print "You are now here: " + Occupant.get_location()
        checkTreasure(Occupant)
    else:
        move(Occupant)


def checkTreasure(Occupant):
    """Determines if the player has won the game or not."""
    if Occupant.location.x == TREASURE_X and Occupant.location.y == TREASURE_Y:
        win(Occupant)


def win(Occupant):
    """Executes the win sequences by printing a message and exits."""
    print "You have found the treasure in %s!" % Occupant.get_location()
    exit()

if __name__ == '__main__':
    print "You awake as a thief in search of gold in front of Divine a",
    print "mystical castle."
    print "You believe the treasure is here; you may choose to enter or leave."
    choice = raw_input("(enter/leave) ")
    if choice == "enter":
        thief = Occupant()
        while True:
            move(thief)
    else:
        print "You leave immediately."
        exit()
