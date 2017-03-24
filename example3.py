age=int(input('enter age: '))
if age<0:
    print('inavaid age')
elif age<1:
    print('youre an infant')
elif age<=12:
    print( 'youre just a kid')
elif age<=19:
    print('youe a teenger')
elif age<=45:
    print('youre a adult')
elif age<=59:
    print('you are middle-aged')
elif age>=60 and age<=120:
    print(' you are old ')
else:
    print('your are too old but still alive')