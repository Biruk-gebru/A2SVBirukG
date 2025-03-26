# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bn(left:int,right:int)->int:
            if left>right:
                return -1
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return bn(mid+1,right)
            else:
                return bn(left,mid-1)
        return bn(0,len(nums)-1)