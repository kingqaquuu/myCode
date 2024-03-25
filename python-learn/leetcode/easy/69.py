'''
Author: kingqaquuu
Date: 2024-03-19 17:27:32
FilePath: \myCode\python-learn\leetcode\easy\69.py
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        left,right = 1,x
        while left<=right:
            mid = left+(right-left)//2
            if mid*mid>x:
                right = mid-1
            else:
                left = mid+1
        return right