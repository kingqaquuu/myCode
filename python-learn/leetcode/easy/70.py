'''
Author: kingqaquuu
Date: 2024-03-19 17:31:49
FilePath: \myCode\python-learn\leetcode\easy\70.py
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        for i in range(n-1):
            a,b=b,a+b
        return b