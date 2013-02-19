#options = ['hello','how','are','you']
#
#for items in options:
#    print items

def jump():
    return "You jumped!"

# dicts
actions = {'jump': jump}

print "What action?"
for items in actions:
    print items

prompt = "> "
choice = raw_input(prompt)

command = actions[choice]
command()

# do 'actions = [jump, attack]' and then 'action[0]()'
# think of '()' as the "call" operator

# class practice

class blankCharacter:
    HP = 0
    MP = 0

class Mage:
    HP = 100
    MP = 500
    def description():
        return "You are now an amazing wizard."
    def g():
        return 'hello world'
    h = g()
    d = description()

print blankCharacter.HP + Mage.HP

character = Mage()

print character.MP
print Mage.h
print character.h

blankCharacter = Mage
print blankCharacter.HP
print Mage.d
