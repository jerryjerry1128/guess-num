import random

r = random.randint(1, 100)
while True:
    num = input('guess number: ')
    num = int(num)
    if num == r:
        print('You got it ! ')
        break
    elif num > r:
        print('bigger than answer! ')
    elif num <r:
        print('smaller than answer! ')