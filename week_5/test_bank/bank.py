def main():
    money = value(str(input('Greeting: ')))
    print(f'${money}')

def value(greeting):
    if 'hello' in greeting.lower().split()[0]:
        return 0
    elif greeting.lower()[0] == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()