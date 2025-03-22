# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sunsets=[]
        for i in range(1<<(len(nums))):
            sub=[]
            for j in range(len(nums)):
                if i & (1<<j):
                    sub.append(nums[j])
            sunsets.append(sub)
        return (sunsets)
        