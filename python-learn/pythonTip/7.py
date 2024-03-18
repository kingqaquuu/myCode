'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\7.py
定义函数is_plural()，参数为term(输入的单词)。
在函数内，如果单词以s结尾，则返回True，否则返回False。
'''
def is_plural(term):
    # 此处编写代码 
    if term.endswith('s'):
        return True
    else:
        return False
# 获取输入 
input_word = input()

# 调用函数并输出结果 
print(is_plural(input_word))