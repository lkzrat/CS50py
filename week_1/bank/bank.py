greet = str(input('Greeting: ')).strip().lower()
if 'hello' in greet:
    print('$0')
elif greet[0] == 'h':
    print('$20')
else:
    print('$100')