# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        sol = 0
        while i < j:
            sol = max(sol, (j -i)*min(height[j],height[i]))
            if height[j] < height[i]:
                j -= 1
            elif height[j] > height[i]:
                i+=1
            else:
                i += 1
        return sol