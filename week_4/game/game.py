import random as rd
import sys

def main():
    num = get_num()
    while True:
        try:
            guess = int(input('Guess: '))
        except ValueError:
            pass
        else:
            if guess < num:
                print('Too small!')
            elif guess > num:
                print('Too large!')
            else:
                sys.exit('Just right!')

def get_num():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
        else:
            if level <= 0:
                pass
            else:
                break
    return rd.randint(1, level)

main()