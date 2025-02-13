# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        Window = 0
        count = 0
        left = 0
        kn = k 
        for right in range(n):
            if nums[right] == 0:
                count += 1
            Window += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                Window -= 1
                left += 1
               
            ans = max(ans, Window) 

        return ans

        