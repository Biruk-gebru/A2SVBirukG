# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sol=[]
        i=0
        while i<len(nums):
            corr=nums[i]-1
            if nums[i]!=nums[corr]:
                temp=nums[i]
                nums[i]=nums[corr]
                nums[corr]=temp
            else:
                i+=1
        print(nums)
        for i in range(len(nums)):
            if nums[i]!=i+1:
                sol.append(nums[i])
        return sol
        