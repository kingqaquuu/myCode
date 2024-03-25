'''
Author: kingqaquuu
Date: 2024-03-18 19:04:08
FilePath: \myCode\python-learn\leetcode\20.py
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return not stack