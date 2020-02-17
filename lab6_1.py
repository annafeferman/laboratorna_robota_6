days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)

while True:
    while True:
        try:
            d, m, y = int(input('Day: ')), \
                      int(input('Month: ')), \
                      int(input('Year: '))
            break
        except(ValueError, TypeError):
            print('Enter correct number')

    if d in days and m in months and y in years:
        if y % 4 == 0:
            if d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                if m == 12:
                    m = 0
                    y_2 = y + 1
                    m_2 = m + 1
                    print(f'Next day 1.{m_2}.{y_2}')
                    print(f'Previous day {d - 1}.12.{y}')
                else:
                    if m == 1:
                        print(f'Next day 1.{m + 1}.{y}')
                        print(f'Previous day {d - 1}.{m}.{y}')
                    else:
                        print(f'Next day 1.{m + 1}.{y}')
                        print(f'Previous day {d - 1}.{m - 1}.{y}')
            elif d == 29 and m == 2:
                print(f'Next day 28.2.{y}')
                print(f'Previous day 1.3.{y}')
            elif d == 30 and (m == 9 or m == 4 or m == 6 or m == 11):
                print(f'Next day 29.{m}.{y}')
                print(f'Previous day 1.{m}.{y}')
            else:
                if d == 1:
                    if m == 4 or m == 6 or m == 8 or m == 9 or m == 11 or m == 1 or m == 2:
                        print(f'Next day {d + 1}.{m}.{y}')
                        print(f'Previous day 31.{m - 1}.{y}')
                    elif m == 5 or m == 10 or m == 12 or m == 7:
                        print(f'Next day {d + 1}.{m}.{y}')
                        print(f'Previous day 30.{m - 1}.{y}')
                    else:
                        print(f'Next day {d + 1}.{m}.{y}')
                        print(f'Previous day 29.{m - 1}.{y}')
                else:
                    print(f'Next day {d + 1}.{m}.{y}')
                    print(f'Previous day {d - 1}.{m}.{y}')
        else:
            if d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                if m == 12:
                    m = 0
                    y_2 = y + 1
                    m_2 = m + 1
                    print(f'Next day 1.{m_2}.{y_2}')
                    print(f'Previous day {d - 1}.12.{y}')
                else:
                    if m == 1:
                        print(f'Next day 1.{m + 1}.{y}')
                        print(f'Previous day {d - 1}.{m}.{y}')
                    else:
                        print(f'Next day 1.{m + 1}.{y}')
                        print(f'Previous day {d - 1}.{m}.{y}')
            elif d == 28 and m == 2:
                print(f'Next day 1.3.{y}')
                print(f'Previous day 27.2.{y}')
            elif d == 30 and (m == 9 or m == 4 or m == 6 or m == 11):
                print(f'Next day 29.{m}.{y}')
                print(f'Previous day 1.{m}.{y}')
            else:
                if d == 1:
                    if m == 4 or m == 6 or m == 8 or m == 9 or m == 11 or m == 1 or m == 2:
                        print(f'Next day {d + 1}.{m}.{y}')
                        print(f'Previous day 31.{m - 1}.{y}')
                    elif m == 5 or m == 10 or m == 12 or m == 7:
                        print(f'Next day {d + 1}.{m}.{y}')
                        print(f'Previous day 30.{m - 1}.{y}')
                    else:
                        print(f'Next day {d + 1}.{m}.{y}')
                        print(f'Previous day 28.{m - 1}.{y}')
                else:
                    print(f'Next day {d + 1}.{m}.{y}')
                    print(f'Previous day {d - 1}.{m}.{y}')

    print(f'Do you want to run the program again?')
    text = input('Input "Yes" or "No": ')
    if text == 'Yes':
        continue
    else:
        break
