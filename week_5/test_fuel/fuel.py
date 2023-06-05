def main():
    while True:
        fuel = str(input('Fraction: '))
        try:
            fuel = gauge(convert(fuel))
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    print(fuel)

def convert(fraction):
    x = int(fraction.replace('/', ' ').split()[0])
    y = int(fraction.replace('/', ' ').split()[1])
    if x <= y or y == 0:
        return round((x/y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage:.0f}%'


if __name__ == "__main__":
    main()