# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        count = len(costs)//2
        sol = 0
        for i in range(len(costs)):
            if count:
                sol += costs[i][0]
                count -= 1
            else:
                sol += costs[i][1]
        return sol
        
        