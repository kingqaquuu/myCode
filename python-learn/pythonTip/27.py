'''
Author: kingqaquuu
Date: 2024-03-16 19:39:21
FilePath: \myCode\python-learn\pythonTip\27.py
编写一个程序来翻转给定句子中的单词顺序。

定义函数reverse_sentence_words()，该函数接受一个参数sentence(表示句子)。
该函数应该返回翻转其单词顺序的句子。
考虑任何由空格字符分隔的序列作为一个单词。
不要在句子的开头或结尾添加额外的空格。
'''
def reverse_sentence_words(sentence):
    # 此处写你的代码
    sentence = sentence.split()
    sentence.reverse()
    return ' '.join(sentence)
# 获取输入
sentence = input()
# 调用函数并打印结果
print(reverse_sentence_words(sentence))