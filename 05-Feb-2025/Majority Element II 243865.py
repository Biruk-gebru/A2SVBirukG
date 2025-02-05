# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        nums_c = Counter(nums)
        sol = []
        for k,v in nums_c.items():
            if v>n:
                sol.append(k)
        return sol
        