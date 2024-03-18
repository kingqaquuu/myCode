'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\17.py
编写一个Python程序，找出列表中第n小的整数。

定义函数find_nth_smallest()，该函数接受整数列表numbers_list和整数n作为参数。
在函数内部，返回列表中第n小的整数。
如果n大于列表的长度，则返回None。
'''
def find_nth_smallest(numbers_list, n):
    # 此处编写你的代码
    numbers_list.sort()
    return numbers_list[n-1] if n<=len(numbers_list) else None
# 将输入的整数转换为列表
numbers_list = list(map(int, input().split()))
# 获取n的输入
n = int(input())
# 调用函数
print(find_nth_smallest(numbers_list, n))