# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count =0
        for elem in nums:
            if elem == 1:
                count += 1
            else:
                count = 0
            max_count = max(max_count , count)
        return max_count
            

        