'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\18.py
编写一个函数，用于求两个整数的最大公约数（GCD）。

定义函数find_gcd()，有两个数字参数a和b。
在函数内部，返回a和b的最大公约数。
'''
def find_gcd(a, b):
    # 在此处编写代码
    if a>b:
        a,b = b,a
    while b%a!=0:
        a,b = b%a,a
    return a
# 输入整数
first_number = int(input())
second_number = int(input())
# 调用函数
print(find_gcd(first_number, second_number))