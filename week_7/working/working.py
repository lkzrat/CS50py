import re

def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if hour := re.search(r'^([0-1]?[0-9]:?[0-6]?[0-9]?) (AM|PM) to ([0-1]?[0-9]:?[0-6]?[0-9]?) (AM|PM)$', s):
        new_hour = []
        for i in (1, 3):
            t = hour.group(i + 1)
            if len(hour.group(i).split(':')) > 1:
                h1, h2 = hour.group(i).split(':')
                h1, h2 = int(h1), int(h2)
            else:
                h1, h2 = int(hour.group(i)), 0
            if h1 > 12 or h2 >= 60:
                raise ValueError('Invalid hour')
            if  t == 'PM':
                if h1 != 12:
                    h1 += 12
            if t == 'AM' and h1 == 12:
                h1 = 0
            new_hour.append(f'{h1:0>2}:{h2:0>2}')
        return f'{new_hour[0]} to {new_hour[1]}'
    else:
        raise ValueError('Invalid format or input is not an hour')


if __name__ == "__main__":
    main()