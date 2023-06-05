import requests
import sys

def main():
        try:
            value = str(btc_value() * btc_num())
            print('$' + thousand(value))
        except requests.RequestException:
            sys.exit('Error with api link')

def btc_num():
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')
    except IndexError:
        sys.exit('Missing command-line argument')

def btc_value():
    btc_value = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    try:
        return float(btc_value['bpi']['USD']['rate_float'])
    except ValueError:
        sys.exit('No float value found')

def thousand(string):
    n = string.index('.')
    q = len(string[:n])
    string = list(string)
    for i in range(q, 0, -3):
        if i != q:
            string[i - 1] += ','
    return ''.join(string)

main()