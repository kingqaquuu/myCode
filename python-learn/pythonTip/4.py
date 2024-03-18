'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\4.py
编写一个程序，返回整数列表中的最后一个元素。

定义函数last_element()的函数，参数为列表my_list。
在函数中，返回列表的最后一一个元素。
'''
def last_element(my_list):
    # 在此处编写代码
    length = len(my_list)
    return my_list[length-1]
# 获取整数输入，并将其转换为列表
input_list = list(map(int, input().split()))

# 调用函数
print(last_element(input_list))