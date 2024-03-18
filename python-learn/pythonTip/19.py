'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\19.py
编写一个程序来检查一个字符串是否以另一个字符串结尾。

定义函数ends_with()，有两个参数string1和string2。
在函数内，如果string1以string2结尾，则返回True，否则返回False。
'''
def ends_with(string1, string2):
    # 此处写你的代码
    return string1.endswith(string2)
# 获取输入字符串
string1 = input()
string2 = input()
# 调用函数
print(ends_with(string1, string2))