# Problem: Minimize Maximum Pair Sum in Array - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sol = 0
        for i in range(len(nums)//2):
            sol = max(sol , nums[i] + nums[(i+1) * -1] )

        return sol
        