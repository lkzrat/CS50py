import re, sys, inflect
from datetime import date

def main():
    birth = get_date(input('Date of birth: '))
    today = get_date(str(date.today()))
    print(min_alive(str(today - birth)))


def get_date(d):
    try:
        if d_list := re.search(r'^([0-9]{4})-([0-9]{2})-([0-9]{2})$', d):
            year, month, day = d_list.groups()
            year, month, day = int(year), int(month), int(day)
            return date(year, month, day)
        else:
            sys.exit('Invalid date format')
    except ValueError:
        sys.exit('Invalid date')


def min_alive(days):
    day = re.search('^([0-9]+)', days)
    return str(inflect.engine().number_to_words(int(day.group(1)) * 24 * 60).capitalize().replace(' and ', ' ') + ' minutes')


if __name__ == "__main__":
    main()