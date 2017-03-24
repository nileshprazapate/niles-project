point1=float(input('entered co ordinate of x : '))
point2=float(input('entered co ordinate of y : '))
if point1>0 and point2>0:
    print('lies on 1st')
elif point1>0 and point2<0:
    print('lies on 4nd')
elif point1<0 and point2<0:
    print('lies on 3rd')
elif point1<0and point2>0:
    print('lies on 2nd')
else:
    print('invaild')
 
