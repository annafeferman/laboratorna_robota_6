from enum import Enum


class Converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


while True:
    while True:
        try:
            x = float(input('Amount of money: '))
            p = Converter[input('Input currency: ')]
            break
        except(ValueError, TypeError):
            print('Wrong! Try again.')
    if p.value == 1:
        x *= 24.52
        print(x)
    elif p.value == 2:
        x *= 26.75
        print(x)
    elif p.value == 3:
        x *= 1.08
        print(x)
    else:
        x *= 6.29
        print(x)
    print(f'Do you want to run the program again?')
    text = input('Input "Yes" or "No": ')
    if text == 'Yes':
        continue
    else:
        break