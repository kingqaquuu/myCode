'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\9.py
编写一个程序，创建一个给定范围内的整数列表。

定义函数list_between()，有两个参数start和end。
在函数内，创建一个介于start（不包括）和end（不包括）之间的所有整数的列表，并返回该列表。
'''
def list_between(start, end):
    # 此处写你的代码
    return list(range(start+1, end))
# 获取输入的start 及 end
start = int(input())
end = int(input())

# 调用函数
print(list_between(start, end))