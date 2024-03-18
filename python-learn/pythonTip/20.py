'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\20.py
编写一个程序来计算字符串中所有数字的乘积。

定义函数multiply_numbers_in_string()，参数为num_string。
在函数内部，返回字符串中所有数字的乘积。
'''
def multiply_numbers_in_string(num_string):
    # 将字符串输入转换为列表
    num_list = list(map(int, num_string.split()))
    # 在此处编写你的代码
    result = 1
    for i in num_list:
        result *= i
    return result
# 获取输入字符串
num_string = input()
# 调用函数
print(multiply_numbers_in_string(num_string))