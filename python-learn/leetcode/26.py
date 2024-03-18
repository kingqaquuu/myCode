'''
Author: kingqaquuu
Date: 2024-03-18 19:35:39
FilePath: \myCode\python-learn\leetcode\26.py
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow,fast=0,1
        while fast<len(nums):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
            fast+=1
        return slow+1