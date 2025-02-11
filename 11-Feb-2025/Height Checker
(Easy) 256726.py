# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex = sorted(heights)
        sol = 0
        for i in range(len(heights)):
            if heights[i] != ex[i]:
                sol += 1
        return sol

        