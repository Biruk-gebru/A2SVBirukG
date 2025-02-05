# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:  
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:  
        sumE = sum(num for num in nums if num % 2 == 0)  
        sol = []  
        
        for val, index in queries:  
            if nums[index] % 2 == 0:  
                sumE -= nums[index]  
            nums[index] += val  
            
            if nums[index] % 2 == 0:  
                sumE += nums[index]  
            sol.append(sumE)  
        
        return sol  