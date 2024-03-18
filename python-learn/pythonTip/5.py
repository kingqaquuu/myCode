'''
编写一个程序来检查两个字符串是否具有相同数量的字符。

定义函数compare_length()，有两个参数str1和str2。
在函数内，如果str1的长度等于str2的长度，则返回True，否则返回False。
'''
def compare_length(str1, str2):
    # 此处编写你的代码 
    if len(str1)==len(str2):
        return True
    else:
        return False
# 获取输入 
input_str1 = input()
input_str2 = input()

# 调用函数 
print(compare_length(input_str1, input_str2))