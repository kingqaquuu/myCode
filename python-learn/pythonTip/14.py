'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\14.py
编写一个Python程序来判断两个给定的字符串是否是错位词。

如果两个字符串具有相同的字符，但顺序不同，则被认为是彼此的错位词。 例如，restful和fluster是错位词。

定义函数are_anagrams()，有两个参数：string1和string2。
在函数内，如果两个字符串是错位词，则返回True，否则返回False。
'''
import string
def are_anagrams(string1, string2):
    # 此处编写代码 
    str1=string1.lower().replace(' ','')
    str2=string2.lower().replace(' ','')
    if len(str1)!=len(str2):
        return False
    for i in str1:
        if i not in str2:
            return False
        if str1.count(i)!=str2.count(i):
            return False
    if str1==str2:
        return False
    else:
        return True
    
        
# 获取输入string1 和 string2 
string1 = input()
string2 = input()
# 调用函数并打印结果 
print(are_anagrams(string1, string2))