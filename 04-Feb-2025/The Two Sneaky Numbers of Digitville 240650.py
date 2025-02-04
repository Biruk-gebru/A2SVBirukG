# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n_c = Counter(nums)
        sol = []
        for k,v in n_c.items():
            if v == 2:
                sol.append(k)
        return sol
        