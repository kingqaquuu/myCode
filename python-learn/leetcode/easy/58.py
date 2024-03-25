'''
Author: kingqaquuu
Date: 2024-03-19 17:11:57
FilePath: \myCode\python-learn\leetcode\58.py
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        if len(s) == 0:
            return 0
        return len(s[-1])