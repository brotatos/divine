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

# 21:47:08         bob2 | brotatos, no, you'd do 'actions = [jump, attack]' and then 'action[0]()'
# 21:47:16         bob2 | brotatos, think of '()' as the "call" operator
