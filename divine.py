#######################       N
#                     #     W   E
# u_l     u_m     u_r #       S
# 1##     2##     3## #
# ###     ###     ### #
# ###     ###     ### #
#                     #
# m_l     m_m     m_r #
# 4##     5##     6## #
# ###     ###     ### #
# ###     ###     ### #
#                     #
# b_l     b_m     b_r #
# 7##     8##     9## #
# ###     ###     ### #
# ###     ###     ### #
#                     #
#        enter        #
#######################

import random
import environment

print """You awake as a thief in search of gold in front of Divine, a mystical castle.
You believe the treasure is here; however, you may choose to enter or leave.
"""

def enter():
    bottom_middle();

def bottom_middle():
    print "You enter the divine castle.\n"
    print "You have three rooms you may go through:"
    print "\tleft\n\tforward\n\tright\t"

    while True:
        direction = raw_input("> ");
        if direction == "left":
            bottom_left()
        elif direction == "forward":
            middle_middle()
        else:
            bottom_right()

enter()
