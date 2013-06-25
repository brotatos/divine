options = ['hello','how','are','you']

#for items in options:
#    print items

def jump():
    print "You jumped!"

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
