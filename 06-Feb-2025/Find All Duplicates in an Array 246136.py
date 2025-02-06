# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s_co = Counter(nums)
        sol = []
        for k,v in s_co.items():
            if v != 1:
                sol.append(k)
        return sol



        