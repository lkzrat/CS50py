def main():
    print(shorten(str(input('word: '))))


def shorten(word):
    for v in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
       word = word.replace(v, '')
    return word


if __name__ == "__main__":
    main()