def main():
    date = get_date()
    print(date_convertion(date))

def get_date():
    while True:
        date = str(input('Date: '))
        if date_check(date):
            return date

def date_check(date):
    if ('/' in date) == False and (',' in date) == False:
        return False
    if '/' in date:
        if verify_string(''.join(date_sep(date))):
            return False
        if int(date_sep(date)[0]) > 12 or int(date_sep(date)[0]) < 1:
            return False
        if int(date_sep(date)[1]) > 31 or int(date_sep(date)[1]) < 1:
            return False
        else:
            return True
    if ',' in date:
        if date_sep(date)[0].isnumeric():
            return False
        if (1 < int(date_sep(date)[1]) < 30) == False:
            return False
        else:
            return True

def date_sep(date):
    if '/' in date:
        return date.replace('/', ' ').split()
    else:
        date = date.split()
        date[1] = date[1].replace(',', '')
        return date

def date_convertion(date):
    date = date_sep(date)
    if verify_string(''.join(date)):
        while True:
            try:
                date[0] = month.index(date[0].title()) + 1
            except KeyError:
                pass
            else:
                return f'{date[2]}-{date[0]:0>2}-{date[1]:0>2}'
    else:
        return f'{date[2]}-{date[0]:0>2}-{date[1]:0>2}'

def verify_string(string):
    for i in range(len(string)):
        if string[i].isalpha():
            return True
        else:
            return False

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

main()