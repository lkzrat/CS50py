def main():
    order()

def order():
    total = 0
    while True:
        try:
            o = float(menu[str(input('Item: ')).title()])
        except KeyError:
            pass
        except EOFError:
            break
        else:
            total += o
            print(f'Total: ${total:.2f}')

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()