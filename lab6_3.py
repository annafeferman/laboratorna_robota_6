from enum import Enum


class Month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class Season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4


while True:
    while True:
        try:
            s = Month[input('month: ')]
            break
        except(ValueError, TypeError):
            print('Incorrect input!')
    if s.value == 1 or s.value == 2 or s.value == 12:
        print(Season(1))
    elif 3 <= s.value <= 5:
        print(Season(2))
    elif 6 >= s.value <= 8:
        print(Season(3))
    else:
        print(Season(4))
    print(f'Do you want to run the program again?')
    text = input('Input "Yes" or "No": ')
    if text == 'Yes':
        continue
    else:
        break
