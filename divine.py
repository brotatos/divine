#!/usr/bin/env python
"""
Copyright (c) 2012-2013 Robin Choudhury

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

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
"""

from random import randrange
import sys

TREASURE_X = randrange(0, 2)
TREASURE_Y = randrange(0, 2)
X_MIN = 0
X_MAX = 2
Y_MIN = 0
Y_MAX = 2


class Occupant(object):
    """Represents the player navigating through the maze."""

    def __init__(self):
        self.location = {'x': randrange(0, 2), 'y': randrange(0, 2)}
        self.names = [
            ("The Solar", "The Mezzanine", "The Lords & Ladies ", "Chamber"),
            ("The Bower", "The Great Hall", "The Bottlery"),
            ("The Chapel", "The Oratory", "The Bailey")
            ]

    def get_directions(self):
        """Obtains possible directions based off current coordinates."""
        dirs = set()

        if self.location['x'] > X_MIN:
            dirs.add("west")

        if self.location['x'] < X_MAX:
            dirs.add("east")

        if self.location['y'] > Y_MIN:
            dirs.add("south")

        if self.location['y'] < Y_MAX:
            dirs.add("north")

        return dirs

    def _get_location(self):
        """Assigns room names to rooms based of cartesian coordinates."""
        return self.names[self.location['x']][self.location['y']]

    def move(self):
        """Move occupant based off direction. Print the current room
        location."""

        print("\nYou are currently at: {0} ".format(self._get_location()))
        print("Which direction would you like to go?")
        dirs = self.get_directions()
        for i in dirs:
            print("\t{0}".format(i))

        direction = input("> ")

        if direction in dirs:
            if direction == "east":
                self.location['x'] += 1
            elif direction == "west":
                self.location['x'] -= 1
            elif direction == "north":
                self.location['y'] += 1
            else:
                self.location['y'] -= 1
            print("You are now here: {0}".format(self._get_location()))
            self.check_treasure()
        else:
            self.move()

    def check_treasure(self):
        """Determines if the player has won the game or not."""
        if self.location['x'] == TREASURE_X \
                and self.location['y'] == TREASURE_Y:
            self.win()

    def win(self):
        """Executes the win sequences by printing a message and exits."""
        print("You have found the treasure in " +
              "{0}!".format(self._get_location()))
        sys.exit(0)

if __name__ == '__main__':
    print("""
    You awake as a thief in search of gold in front of Divine a mystical castle
    You believe the treasure is here; you may choose to enter or leave.
    """)
    if input("(enter/leave) ") == "enter":
        THIEF = Occupant()
        while True:
            THIEF.move()
    else:
        print("You leave immediately.")
        sys.exit()
