'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\24.py
编写一个程序，求出给定数字区间内的所有偶数。

定义函数find_even_numbers()，参数为num。
在函数内部，使用列表推导式从1到num查找所有偶数，并返回该列表。
如果num <= 1，则返回空列表[]。
'''
def find_even_numbers(num):
    # 此处写入代码 
    a=[i for i in range(1,num+1) if i%2==0]
# 获取整数输入
num = int(input())
# 调用函数
print(find_even_numbers(num))