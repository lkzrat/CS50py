def main():
    names = []
    while True:
        try:
            names.append(str(input('Name: ')))
        except EOFError:
            break
    print(adieu(names))

def adieu(names):
    if len(names) == 2:
        return f'Adieu, adieu, to {names[0]} and {names[1]}'
    elif len(names) > 2:
        for i in range(len(names) - 1):
            names[i] += ', '
        names[-1] = f'and {names[-1]}'
        names = ''.join(names)
        return f'Adieu, adieu, to {names}'
    else:
        return f'Adieu, adieu, to {names[0]}'

main()