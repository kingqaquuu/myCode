'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\13.py
编写一个程序，返回一个数字的数字列表，但需要以相反的顺序排列。

定义函数reverse_number_digits()，参数为一个数字num。
在函数内，将数字num转换为其相反顺序的数字列表。
'''
def reverse_number_digits(num):
    # 在此处编写你的代码
    return list(map(int, str(num)[::-1]))
# 获取用户输入
num = int(input())

# 调用函数
print(reverse_number_digits(num))