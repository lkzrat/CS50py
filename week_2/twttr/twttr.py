def main():
    i = str(input('Input: '))
    print(f'Output: {twttr(i)}')

def twttr(w):
    word = list(w)
    for i in range(len(word)):
        if word[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            word[i] = ''
    word = ''.join(word)
    return word

main()