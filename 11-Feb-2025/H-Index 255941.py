# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        sol = 0
        for i in range(len(citations)):
            temp = len(citations) - i
            if temp >= citations[i]:
                sol = citations[i]

            sol = max(sol, min(citations[i], temp))
        return sol

        