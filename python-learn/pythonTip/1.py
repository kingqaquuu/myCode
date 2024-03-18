'''
Author: kingqaquuu
Date: 2024-03-16 19:28:27
FilePath: \myCode\python-learn\pythonTip\1.py
编写一个程序将分钟转换为秒。

定义函数convert_to_seconds()，参数为minutes。
在函数内，将分钟转换为秒（1分钟=60秒），并返回结果。
'''
def convert_to_seconds(minutes):
    return minutes * 60

    # 输入分钟
input_minutes = int(input())
    # 调用函数 
print(convert_to_seconds(input_minutes))