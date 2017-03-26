n=0
sum=0
while n<5:
    value=input('enter value of %s:'%(n+1))
    sum = sum + float(value)
    n += 1
print('sum = %.2f'% sum)



n=0
sum=0
while n<5:
    value=input('enter value of %s:'%(n+1))
    try:
        sum = sum + float(value)
        n += 1
    except ValueError:
        print('invaild input. please enter  numeric value')
print('sum = %.2f'% sum)