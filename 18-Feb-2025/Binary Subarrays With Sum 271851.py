# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        s=0
        res = 0
        for n in nums:
            s += n
            if (s-k) in dic:
                res += dic[s-k]
            dic[s] = dic.get(s,0) + 1
        return res

        