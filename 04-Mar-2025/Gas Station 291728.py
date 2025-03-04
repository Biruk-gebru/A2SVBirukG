# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            gas[i]=gas[i]-cost[i]
        if sum(gas)<0:
            return -1
        sm=0
        ans=0
        for i in range(len(gas)):
            sm=sm+gas[i]
            if sm<0:
                sm=0
                ans = i + 1
                
        return ans