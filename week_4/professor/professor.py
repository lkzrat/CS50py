import random

def main():
    generate_integer(get_level())

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if 1 <= level <= 3:
                return level
                break
        except ValueError:
            pass

def get_user(x, y):
    try:
        return int(input(f'{x} + {y} = '))
    except ValueError:
        return 'error'

def get_num(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

def generate_integer(level):
    score = 0
    for i in range(10):
        x = get_num(level)
        y = get_num(level)
        tries = 0
        while True:
            if tries == 3:
                print(f'{x} + {y} = {x + y}')
                break
            user = get_user(x, y)
            if user == (x + y):
                score += 1
                break
            else:
                print('EEE')
                tries += 1
    print(f'Score: {score}')

if __name__ == "__main__":
    main()