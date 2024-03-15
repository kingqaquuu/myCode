def is_leap_year(year):
    return year%4==0 and year%100!=0 or year%400==0
def main():
    date=int(input('请输入日期:(示例:20180101)'))
    year=date//10000
    month=date%10000//100
    day=date%100
    months={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if month>=3:
        if is_leap_year(year):
            months[2]=29
            for i in range(1,month):
                day+=months[i]
        else:
            months[2]=28
            for i in range(1,month):
                day+=months[i]
    else:
        for i in range(1,month):
            day+=months[i]
    print('这是{}年的第{}天'.format(year,day))
if __name__ == '__main__':
    main()