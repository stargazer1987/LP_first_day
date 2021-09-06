import random

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
 #   except ZeroDivisionError:
 #       print("Не могу поделить на 0")
 #   except TypeError:
 #       print("Функция принимает число")
    except (ZeroDivisionError, TypeError):
        print('Не могу поделить')

cut_cake('5')
cut_cake(0)

while True:
    p = random.randint(1,10)
    cut_cake(p)