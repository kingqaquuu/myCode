'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\21.py
编写一个程序来检查一个单词是否为同源词。
同源词是指不包含任何重复字母的单词，例如brown，fox，quick等。

定义函数is_string_isogram()，参数为一个单词word。
在函数内，如果单词是同源词，则返回True，否则返回False。
'''
def is_string_isogram(word):
    # 将单词转换为小写
    word = word.lower()
    # 在此处编写你的代码
    for i in word:
        if word.count(i) > 1:
            return False
    return True
# 从用户处获取输入
word = input()
# 调用函数
print(is_string_isogram(word))