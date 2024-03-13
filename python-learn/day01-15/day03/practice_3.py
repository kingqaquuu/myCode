a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a+b>c and b+c>a and a+c>b:
    print('周长：%d'%(a+b+c))
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print('面积：%f'%area)
else:
    print('不能构成三角形')