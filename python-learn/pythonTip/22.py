'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\22.py
编写一个程序来计算整数的二进制表示中1的个数。

定义函数count_binary_ones()，参数为数字num。
在函数内，将数字转换为其二进制表示，并计算“1”的个数。
'''
def count_binary_ones(num):
    # 此处写你的代码 
    return bin(num).count('1')
# 从标准输入读取一个整数
num = int(input())
# 调用函数
print(count_binary_ones(num))