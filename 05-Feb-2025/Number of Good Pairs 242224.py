# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        i, j, counter = 0, 1, 0
        while j < len(nums):
            if nums[i] == nums[j]:
                counter += j - i
                j += 1
            else:
                i = j
                j += 1
        return counter



        