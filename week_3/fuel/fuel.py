def main():
    num = input('Fraction: ')
    if verify(num):
        fuel = percent(num)
        if fuel <= 1:
            print('E')
        elif fuel >= 99:
            print('F')
        else:
            print(f'{fuel:.0f}%')
    else:
        main()

def percent(e):
    bar_pos = e.index('/')
    x = float(e[:bar_pos])
    y = float(e[bar_pos + 1:])
    if x > y or y == 0:
        main()
    else:
        result = float((x / y)*100)
        return result

def verify(n):
    if bool('/' in n) == False:
        return False
    bar_pos = n.index('/')
    if n[:bar_pos].isalpha() or n[bar_pos + 1:].isalpha():
        return False
    if '.' in n[:bar_pos] or '.' in n[bar_pos + 1:]:
        return False
    else:
        return True
main()