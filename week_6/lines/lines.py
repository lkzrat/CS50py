import sys

def main():
    num_lines = get_lines(get_file())
    print(f'''
- File: {get_file().split('/')[-1]}
- Lines: {num_lines}
    ''')


def get_file():
    try:
        if '.py' not in sys.argv[1]:
            sys.exit('Command-line argument is not a .py file')
        if len(sys.argv) != 2:
            sys.exit('Too many comand-line arguments')
        else:
            return sys.argv[1]
    except IndexError:
        sys.exit('No command-line argument')


def get_lines(py):
    try:
        with open(py) as file:
            num = 0
            for line in file.readlines():
                try:
                    if line.strip()[0] not in ('#', '\n'):
                        num += 1
                except IndexError:
                    pass
            return num
    except FileNotFoundError:
        sys.exit(f'File {py} does not exist')


if __name__ == '__main__':
    main()