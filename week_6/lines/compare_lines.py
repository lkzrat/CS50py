import sys

def main():
    nums = []
    files = get_files()
    for file in files:
        nums.append(get_lines(file))
    big = max(nums, key = int)
    i = nums.index(big)
    print(f'''
- Biggest file: {files[i].split('/')[-1]}
- Lines: {big}
    ''')

def get_files():
    files = []
    try:
        for i in range(len(sys.argv[1:])):
            if '.py' not in sys.argv[i + 1]:
                sys.exit('Command-line argument is not a .py file')
            else:
                files.append(sys.argv[i + 1])
        return files
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