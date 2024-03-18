'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\10.py
编写一个程序来判断一个数字是否为素数。

定义函数check_prime()，参数为一个数字。
在函数内，如果数字为素数，返回True，否则返回False。
'''
def check_prime(num):
    # 在此处编写代码
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
# 输入一个整数
number = int(input())

# 调用函数
print(check_prime(number))