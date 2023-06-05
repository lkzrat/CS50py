def main():
    camel = str(input('camelCase: '))
    print(f'snake_case: {snake(camel)}')

def snake(w):
    word = list(w)
    for i in range(len(word)):
        if word[i].isupper():
            word[i] = f'_{word[i].lower()}'
    word = ''.join(word)
    return word

if __name__ == '__main__':
    main()