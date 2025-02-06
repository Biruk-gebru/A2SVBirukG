# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        sol = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] * nums[j] in sol:
                    ans += sol[nums[i] * nums[j]]
                sol[nums[i]* nums[j]] += 1
        return ans * 8
        
        