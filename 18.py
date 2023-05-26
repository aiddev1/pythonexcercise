import random

numbers= range(1,10)
numfind = random.choice(numbers)
tries = 3

while True:
    guess = input('guess the num: ')
    if guess == numfind:
        print('this is correct')
        exit()
    elif guess != numfind:
        print('not correct')
        tries -=1
        if tries == 0:
            print('you are out of tries')
            exit()