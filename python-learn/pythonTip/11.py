'''
Author: kingqaquuu
Date: 2024-03-16 19:31:46
FilePath: \myCode\python-learn\pythonTip\11.py
编写一个Python程序来计算字符串中元音字母的数量。

定义函数vowel_count()，参数为string(表示字符串)。
在函数中统计字符串中的元音字母数，并返回计数。
'''
def vowel_count(string):
    # 此处写你的代码 
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count+=1
    return count
# 获取输入字符串 
input_string = input()
# 调用函数 
print(vowel_count(input_string))