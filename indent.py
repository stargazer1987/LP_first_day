import random

x = 0
while x < 10:
    print(x)
    x = x + 1

def is_more_than_five(number):
    print('Я в функции')
    if number > 5:
        print('Больше 5')
    else:
        print('Меньше 5')

rand_num = random.randint(1, 10)
is_more_than_five(rand_num)