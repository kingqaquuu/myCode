'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\6.py
编写一个程序来连接字符串的首尾字符。

定义函数join_first_last()，参数为input_str。
在函数内部，返回字符串的首尾字符的连接字符串。
'''
def join_first_last(input_str):
    # 在此处编写你的代码
    length = len(input_str)
    return input_str[0] + input_str[length-1]
# 输入字符串
given_string = input()

# 调用函数
print(join_first_last(given_string))