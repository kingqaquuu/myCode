'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\3.py
编写一个程序，找出列表中最大和最小数字之间的差值。

定义函数difference_max_min()，参数为list_nums。
在函数内部，找出列表中的最大和最小数字，并返回差值
'''
def difference_max_min(list_nums):
    # 在此处编写代码
    return max(list_nums) - min(list_nums)
# 输入整数，并将其转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(difference_max_min(numbers))