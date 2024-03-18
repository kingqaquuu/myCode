'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\8.py
编写一个程序，用于在一组整数中找出唯一的数字。假设列表中只有一个唯一的数字。

定义函数find_unique_number()，参数为num_list，数字列表。
在函数内部，找出只出现一次的数字，并返回它。
如果列表只有一个数字，则返回该数字。
如果列表为空，则返回None。
如果不存在这样的数字，则返回None。
'''
def find_unique_number(num_list):
    # 此处编写你的代码 
    for i in num_list:
        if num_list.count(i) == 1:
            return i
# 将输入的整数转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique_number(numbers))