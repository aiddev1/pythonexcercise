import random

def guess_num():
    num = random.randint(1,100)
    attempts=0
    guessed = False

    print('welcome')
    print('num between 1 to 100')

    while not guessed:
        guess = int(input('enter your guess: '))
        attempts += 1

        if guess == num:
            print('its correct')
            guessed = True
        elif guess < num :
            print('to low')
        else:
            print('too high')
guess_num()