# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        mod = 1
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                if count == 1:
                    return False
                count += 1
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i-1]  
        return True
        