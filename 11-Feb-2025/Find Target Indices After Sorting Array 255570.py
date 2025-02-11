# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        sol=[]
        for i in range(len(nums)):
            if nums[i]==target:
                sol.append(i)
        return sorted(sol)

        