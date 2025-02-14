# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:  
    def minimumAverageDifference(self, nums: List[int]) -> int:  
        total_sum = sum(nums)  
        current_sum = 0  
        min_diff = float('inf')  
        index = -1  
        
        for i in range(len(nums)):  
            current_sum += nums[i]  
            left_avg = current_sum // (i + 1)  
            if i < len(nums) - 1:  
                right_avg = (total_sum - current_sum) // (len(nums) - (i + 1))  
            else:  
                right_avg = 0  
            
            diff = abs(left_avg - right_avg)  
            
            if diff < min_diff:  
                min_diff = diff  
                index = i  
        
        return index  