def main():
    g_list = make_list()
    if len(g_list[0]) < 1:
        pass
    else:
        for i in range(len(g_list[0])):
            print(f'{g_list[1][i]} {g_list[0][i]}')

def make_list():
    items = []
    quantity = []
    while True:
        try:
            item = str(input()).strip().upper()
        except EOFError:
            break
        else:
            if (item in items) == False:
                items.append(item)
                items = sorted(items)
                quantity.append(1)
            else:
                quantity[items.index(item)] += 1
    return (items, quantity)

main()