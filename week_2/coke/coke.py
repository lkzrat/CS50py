amount = 50
while amount > 0:
    print(f'Amnount Due: {amount}')
    coin = int(input('Insert Coin: '))
    if coin in [5, 10, 25]:
        amount -= coin
print(f'Change Owed: {-amount}')