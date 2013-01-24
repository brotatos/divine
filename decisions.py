def confirmation():
#    for foo in bar:
#        do action
#        unless flag:
#           then go back to previous function


def character_choice():
    character = raw_input("monk or warrior(m/w)? ")
    if character == "m":
        confirmation()
        monk()
    if character == "w":
        confirmation()
        warrior()


character_choice()
