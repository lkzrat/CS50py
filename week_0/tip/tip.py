def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = list(str(d))
    dollars.remove('$')
    dollars = ''.join(dollars)
    dollars = float(dollars)
    return dollars


def percent_to_float(p):
    percent = list(str(p))
    percent.remove('%')
    percent = ''.join(percent)
    percent = float(percent)/100
    return percent

main()