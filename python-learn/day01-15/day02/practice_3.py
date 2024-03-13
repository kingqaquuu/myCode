year=int(input('year='))
flag=(year%4==0 and year%100!=0 or year%400==0)
if(flag):
    print('%d是闰年'%year)
else:
    print('%d不是闰年'%year)