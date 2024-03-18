'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\23.py
编写一个程序来计算第n个四面体数。

定义函数calc_tetrahedral_number()，参数第n个数n。
在函数内，使用公式(n*(n+1)*(n+2))/6)计算第n个四面体数，并返回它。
'''
def calc_tetrahedral_number(n):
    # 在此处编写你的代码
    return int((n*(n+1)*(n+2))/6)
# 输入整数
num = int(input())
# 调用函数
print(calc_tetrahedral_number(num))