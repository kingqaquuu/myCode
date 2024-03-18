'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\15.py
编写一个Python程序来确定字符串中的所有字符是否相同。

定义函数is_string_identical()，参数为text_string(字符串)。
在函数内，如果字符串中的所有字符都相同，则返回True，否则返回False。
'''
def is_string_identical(text_string):
    # 此处编写代码
    length = len(text_string)
    for i in text_string:
        if i != text_string[0]:
            return False
    return True
# 获取输入 
text_string = input()
# 调用函数 
print(is_string_identical(text_string))