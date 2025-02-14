# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum , right_sum = 0, sum(nums) - nums[0]
        idx = -1
        if left_sum == right_sum:
                return 0
        for i in range(len(nums)):
            left_sum += nums[i]
            if i !=len(nums) - 1:
                right_sum -= nums[i+1] 
            if left_sum == right_sum:
                idx = i + 1
                break
        if idx == len(nums):
            idx = -1
        return idx
        
        


            
        