def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isnumeric():
        return False
    if bool(2 <= len(s) <= 6) == False:
        return False
    if bool(s[:1].isalpha()) == False:
        return False
    if bool(s.isalpha()) == False:
        for i in range(len(s)):
            if s[i].isnumeric():
                n_pos = i
                break
        if s[n_pos] == '0':
            return False
        if bool(s[n_pos:].isnumeric()) == False:
            return False
    for c in range(len(list(s))):
        if list(s)[c] in ['.', ' ', ',', ';', ':', '?', '!', '\'', '\"', '/']:
            return False
    else:
        return True

main()