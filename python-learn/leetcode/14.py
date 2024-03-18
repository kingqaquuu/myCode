'''
Author: kingqaquuu
Date: 2024-03-18 18:53:28
FilePath: \myCode\python-learn\leetcode\14.py
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        prefix = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix