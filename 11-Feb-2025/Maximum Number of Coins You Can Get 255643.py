# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sol = 0
        piles.sort()
        print(piles)
        for i in range(len(piles)-2,len(piles) - len(piles)//3*2 -1,-2):
            sol += piles[i]
        return sol
        