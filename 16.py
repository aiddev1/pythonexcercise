voted = {}

def check_voter(name):
    if voted.get(name):
        print('kick them out')
    else:
        voted[name] = True
        print('let them in')

check_voter('aidin')
check_voter('aidin')
print(voted)