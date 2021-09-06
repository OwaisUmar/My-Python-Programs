import random

bet = int(input('Your bet from 1 to 10 :  '))
lucky_draw = random.randint(1, 10)
balance = 0
if bet == lucky_draw:
    balance += 1000
else:
    balance -= 100

print('Lucky Draw : ', lucky_draw, '\nYour balance : ', balance)
