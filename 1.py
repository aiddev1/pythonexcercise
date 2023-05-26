import random

def rand_l(s,stop,l):
    return random.sample(range(s,stop),l)
print(rand_l(1,20,5))