while True:
    a = float(input('First Number: '))
    b = float(input('Second Number: '))

    try:
        result = a / b
        print('result={}' .format(result))
    except ZeroDivisionError:
        print('error:zero division error')
    try_again=input('\nTry Again(Y/N)?')
    if try_again.upper() !='Y':
        break
    print('\n')
print('GOODBYE!')