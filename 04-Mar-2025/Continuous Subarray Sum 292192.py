# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:  
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:  
        dic = {0: -1} 
        run_sum = 0  
        
        for i in range(len(nums)):  
            run_sum += nums[i]  
            if k != 0:  
                run_sum %= k  
                
            if run_sum in dic:  
                if i - dic[run_sum] > 1:  
                    return True  
            else:  
                dic[run_sum] = i  

        return False  