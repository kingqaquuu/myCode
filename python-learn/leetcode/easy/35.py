class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lenth=len(nums)
        low,mid,high=0,0,lenth-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return low