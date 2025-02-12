# Problem: Array With Elements Not Equal to Average of Neighbors - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:  
    def rearrangeArray(self, nums: List[int]) -> List[int]:  
        i = 0
        j = len(nums)-1
        sol = []
        nums.sort()
        while i<=j:
            sol.append(nums[i])
            if j > i:
                sol.append(nums[j])
            i+=1
            j -= 1
        return sol