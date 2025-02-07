# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:  
    def maxScoreIndices(self, nums: List[int]) -> List[int]:  
        count1 = sum(nums)  
        count0 = 0         
        max_score = 0       
        result_indices = []  

        
        for i in range(len(nums) + 1):  
            
            current_score = count1 + count0  
            
            
            if current_score > max_score:  
                max_score = current_score  
                result_indices = [i] 
            elif current_score == max_score:  
                result_indices.append(i)  

            if i < len(nums):  
                if nums[i] == 0:  
                    count0 += 1  
                else:  
                    count1 -= 1  

        return result_indices