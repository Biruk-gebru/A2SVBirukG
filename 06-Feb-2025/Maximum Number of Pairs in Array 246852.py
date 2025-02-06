# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        candidate = nums[0]
        count = 1
        sol = [0, 0]
        for i in range(1,len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                candidate = nums[i]
                sol[0] += count//2
                count = 1
        sol[0] += count // 2
        sol[1] = len(nums) - (sol[0]*2)
        return sol


        