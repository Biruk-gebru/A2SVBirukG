# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c=sorted(costs)
        sol=0
        for i in range(len(c)):
            if c[i]<=coins:
                sol+=1
                coins-=c[i]
            if c[i]>coins or coins==0:
                break
        return sol
        