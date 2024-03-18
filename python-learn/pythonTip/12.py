'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\12.py
编写一个程序来求一个给定数字的所有因数。

定义函数find_all_factors()，参数为num。
在函数内部，返回一个列表，列表中的数字是输入数字num的所以因数。
如果输入数字小于1，则返回一个空列表。
'''
def find_all_factors(num):
    # 此处写你的代码 
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors
# 输入一个数字 
num = int(input())

# 调用函数 
print(find_all_factors(num))