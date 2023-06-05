def main():
    v_plate = is_valid(input('Plate: '))
    if v_plate == True:
        print('Valid')
    else:
        print('Invalid')


def is_valid(plate):
    if bool(2 <= len(plate) <= 6) == False:
        return False
    if bool(plate[:1].isalpha()) == False:
        return False
    if bool(plate.isalpha()) == False:
        for i in range(len(plate)):
            if plate[i].isnumeric():
                n_pos = i
                break
        if plate[n_pos] == '0':
            return False
        if bool(plate[n_pos:].isnumeric()) == False:
            return False
    for i in range(len(list(plate))):
        if list(plate)[i] in ['.', ' ', ',', ';', ':', '?', '!', '\'', '\"', '/']:
            return False
    else:
        return True


if __name__ == "__main__":
    main()