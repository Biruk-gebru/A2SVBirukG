# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global = float('-inf')
        max_curr = 0
        min_sum = 0
        for i in range(len(nums)):
            max_curr += nums[i]
            max_global = max(max_global , max_curr - min_sum)
            min_sum = min(max_curr, min_sum)
        return max_global 

