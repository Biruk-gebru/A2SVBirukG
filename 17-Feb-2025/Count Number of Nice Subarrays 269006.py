# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        co = 0
        sol = 0
        while j < len(nums):
            if nums[j] % 2 != 0:
                co += 1
            while co > k:
                if nums[i] % 2 != 0:
                    co -= 1
                i += 1
            if co == k:
                temp = i
                while temp < j and nums[temp] % 2 == 0:
                    temp += 1
                    sol += 1
                sol += 1
            j += 1
        return sol





