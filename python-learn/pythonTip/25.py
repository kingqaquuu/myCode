'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\25.py
编写一个程序来求出前n个奇数。

定义函数find_first_n_odds()，参数为n。
在函数内部，返回前n个奇数的列表。
'''
def find_first_n_odds(n):
    # 此处写你的代码 
    return [i for i in range(1, 2*n, 2)]
# 获取输入n
n = int(input())
# 调用函数
print(find_first_n_odds(n))