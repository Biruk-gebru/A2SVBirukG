# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front_prod  = [1]
        for i in nums:
            front_prod.append(i*front_prod[-1])
        front_prod.pop()
        back_prod = [1]
        for i in range(len(nums)-1,-1, -1):
            back_prod.append(nums[i]*back_prod[-1])
        back_prod.pop()
        back_prod.reverse()
        sol = []
        for l in range(len(nums)):
            sol.append(front_prod[l] * back_prod[l])
        return sol

        
        