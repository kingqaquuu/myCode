'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\26.py
斐波那契数列以0（第0项）和1（第1项）开始，每一项都是前两项的和。

编写一个程序来生成第n个斐波那契数。

定义函数fibonacci_number()，参数为n。
在函数中返回第n个斐波那契数。
'''
def fibonacci_number(n):
    # 在此处编写你的代码
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
# 输入n的整数
n = int(input())
# 调用函数
print(fibonacci_number(n))