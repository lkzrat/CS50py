import csv, sys, tabulate

def main():
    table = csv_dict(get_file())
    print(tabulate.tabulate(table, tablefmt = 'grid', headers = 'firstrow'))


def get_file():
    try:
        if '.csv' not in sys.argv[1]:
            sys.exit('Command-line argument is not a .csv file')
        if len(sys.argv) != 2:
            sys.exit('Too many comand-line arguments')
        else:
            return sys.argv[1]
    except IndexError:
        sys.exit('No command-line argument')


def csv_dict(csv_file):
    try:
        table = []
        with open(csv_file) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
        return table
    except FileNotFoundError:
        sys.exit(f'File {csv_file} does not exist')


if __name__ == '__main__':
    main()