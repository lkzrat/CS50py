import validators

def main():
    print(email(str(input('Email Adress: ').strip())))

def email(s):
    if validators.email(s):
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == '__main__':
    main()