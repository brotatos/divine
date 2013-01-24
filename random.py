import random

# random integer
randint(self, a, b)
    #Return random integer in range [a, b], including both end points.

# random range
randrange(self, start, stop=None, step=1, int=<class 'int'>)
#   Choose a random item from range(start, stop[, step]).
#
#   This fixes the problem with randint() which includes the
#   endpoint; in Python this is usually not what you want.
#
#   Do not supply the 'int' argument.
#
