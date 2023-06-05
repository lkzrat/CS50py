def main():
    expression = str(input('Expression: '))
    math(expression)


def math(e):
    e = e.split()
    x = float(e[0])
    y = e[1]
    z = float(e[2])
    if y == '+':
        print(float(x + z))
    if y == '-':
        print(float(x - z))
    if y == '*':
        print(float(x * z))
    if y == '/':
        print(float(x / z))

main()