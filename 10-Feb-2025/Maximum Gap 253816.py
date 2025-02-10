# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        diff = float('-inf')
        for i in range(len(nums)-1):
            temp = nums[i+1] - nums[i]
            diff = max(diff, temp)
        return diff
        