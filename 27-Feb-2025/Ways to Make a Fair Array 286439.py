# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:  
    def waysToMakeFair(self, nums: List[int]) -> int:  
        total_even = sum(nums[i] for i in range(0, len(nums), 2))  
        total_odd = sum(nums[i] for i in range(1, len(nums), 2))  

        curr_even = 0  
        curr_odd = 0  
        
        sol = 0  
        
        for i in range(len(nums)):  
            if i % 2 == 0:  
                total_even -= nums[i]  
            else:  
                total_odd -= nums[i]  
            
            if curr_even + total_odd == curr_odd + total_even:  
                sol += 1  
            

            if i % 2 == 0:  
                curr_even += nums[i] 
            else:  
                curr_odd += nums[i]  
        
        return sol  