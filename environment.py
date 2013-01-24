def room1():
    print "upper left room"

def room2():
    print "upper mid"

def room3():
    print "upper right"

def room4():
    print "mid left"

def room5():
    print "center (mid mid)"
    print "You see a staircase that leads to a basement. What do you want to do?"
    print """
    Options:
    basement (b)
    """
    action = raw_input(prompt)
    if action == "b":
        basement()

def room6():
    print "mid right"

def room7():
    print "bottom left"

def room8():
    print "bottom mid"

def room9():
    print "bottom right"

def basement():
    print "you enter a dark mysterious room."


def teleport():
    print "What room would you like to teleport too?"
    print """
    OPTIONS:
    upper left room (ulr)
    upper mid (um)
    upper right (ur)
    mid left (ml)
    center (c)
    mid right (mr)
    bottom left (bl)
    bottom mid (bm)
    bottom right (br)
    """
    teleport_location = raw_input(prompt)
    if teleport_location == "upper left room" or teleport_location == "ulr":
        room1()
        teleported = 1
    elif teleport_location == "center" or teleport_location == "c":
        room5()

teleported = 0
prompt = "> "
teleport()
