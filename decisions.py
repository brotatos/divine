def confirmation():
#    for blah in blah:
#        do blah blah blah
#        unless asdfasdf:
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
