'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\16.py
编写一个Python程序，用于确定一个数字列表的乘积是否可以被该列表的和整除。

定义函数is_product_divisible_by_sum()的函数，该函数接受一个整数列表作为参数。
在函数内，如果列表中所有数字的乘积可以被该列表的和整除，则返回True，否则返回False。
'''
def is_product_divisible_by_sum(numbers_list):
    # 此处编写代码 
    product = 1
    for i in numbers_list:
        product *= i
    return product % sum(numbers_list) == 0
# 获取整数输入并将其转换为列表
numbers_list = list(map(int, input().split()))
# 调用函数打印结果
print(is_product_divisible_by_sum(numbers_list))