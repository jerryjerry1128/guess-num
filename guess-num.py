import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('guess number: ')
    num = int(num)
    if num == r:
        print('You got it ! ')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('bigger than answer! ')
    elif num <r:
        print('smaller than answer! ')
    print('這是你猜的第', count, '次')