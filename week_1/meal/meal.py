def main():
    mealtime = convert(str(input('What time is it? ')))
    if 7 <= mealtime <= 8:
        print('breakfast time')
    if 12 <= mealtime <= 13:
        print('lunch time')
    if 18 <= mealtime <= 19:
        print('dinner time')

def convert(time):
    hour = float(time.replace(':', '.'))
    return hour

main()