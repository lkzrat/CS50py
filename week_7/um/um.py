import re

def main():
    print(count(str(input("Text: ")).strip()))


def count(s):
    ums = 0
    if list_um := re.findall(r'(.?um.?)', s, flags=re.IGNORECASE):
        for i in range(len(list_um)):
            flag = str(list_um[i]).lower().replace('um', '')
            if re.search(r'\w', flag):
                pass
            else:
                ums += 1
        return ums
    else:
        return 0


if __name__ == "__main__":
    main()