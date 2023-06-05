import csv, sys

def main():
    clean_file(get_file())
    csv_transform(get_file())


def get_file():
    try:
        if '.csv' not in sys.argv[1] and '.csv' not in sys.argv[2]:
            sys.exit('Command-line argument is not a .csv file')
        if len(sys.argv) > 3:
            sys.exit('Too many command-line arguments')
        if len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
        else:
            return (sys.argv[1], sys.argv[2])
    except IndexError:
        sys.exit('No command-line argument')


def csv_transform(files):
    try:
        csv_before = []
        with open(files[0]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                csv_before.append({'name': row['name'], 'house': row['house']})
        with open(files[1], 'a') as file:
            init_writer = csv.writer(file)
            writer = csv.DictWriter(file, fieldnames = ['first', 'last', 'house'])
            init_writer.writerow(['first', 'last', 'house'])
            for student in csv_before:
                last, first = student['name'].split(', ')
                house = student['house']
                writer.writerow({'first': first, 'last': last, 'house': house})
    except FileNotFoundError:
        sys.exit(f'{files[0]} does not exist')


def clean_file(files):
    try:
        open(files[1])
    except FileNotFoundError:
        pass
    else:
        with open(files[1], 'r+') as file:
            file.truncate(0)


if __name__ == '__main__':
    main()