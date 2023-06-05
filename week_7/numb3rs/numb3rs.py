import re

def main():
    print(validate(input(str('IPv4 Address: ')).strip()))


def validate(ip):
    if matches := re.search(r'^([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])$', ip):
        for i in range(1, 5):
            if 0 <= int(matches.group(i)) <= 255:
                pass
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()