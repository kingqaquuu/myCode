'''
Author: kingqaquuu
Date: 2024-03-18 19:52:22
FilePath: \myCode\python-learn\leetcode\27.py
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow,fast=0,0
        while fast<len(nums):
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow