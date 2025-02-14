# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        s=0
        res = 0
        for n in nums:
            s += n
            if (s-k) in dic:
                res += dic[s-k]
            dic[s] = dic.get(s,0) + 1
        return res
