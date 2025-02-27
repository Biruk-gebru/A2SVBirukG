# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pref = 0
        p1 = p2 = 0
        for n in nums:
            pref += n
            p1 = max(pref, p1)
            p2 = min(pref,p2)
        return (p1 - p2)
        