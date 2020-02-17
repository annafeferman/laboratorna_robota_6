while True:
    while True:
        try:
            t = int(input('Input minutes: '))
            break
        except(ValueError, TypeError):
            print('Incorrect input!')
    if 1 <= (t % 6) <= 3:
        print('Green')
    elif (t % 6) == 4:
        print('Yellow')
    else:
        print('Red')
    print(f'Do you want to run the program again?')
    text = input('Input "Yes" or "No": ')
    if text == 'Yes':
        continue
    else:
        break
