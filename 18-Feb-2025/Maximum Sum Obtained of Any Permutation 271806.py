# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = [0 for _ in range(len(nums) + 1)]
        for r in requests:
            n[r[0]] += 1
            n[r[1] + 1] -= 1
        for i in range(1,len(n)):
            n[i] += n[i-1]
        n.sort(reverse = True)
        nums.sort(reverse = True)
        sol = 0
        for i in range(len(nums)):
            sol += nums[i] * n[i]
        return mod(sol, 10 ** 9 + 7)
        