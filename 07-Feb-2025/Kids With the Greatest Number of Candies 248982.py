# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxK = max(candies)
        sol = [False] * len(candies)
        for elem in range(len(candies)): 
            if (candies[elem] + extraCandies) >= maxK:
                sol[elem] = True
        return sol

        