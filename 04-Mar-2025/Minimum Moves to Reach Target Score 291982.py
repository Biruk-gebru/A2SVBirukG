# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        sol = 0
        while target > 1:
            if target % 2 != 0:
                target -= 1
            elif target % 2 == 0:
                if maxDoubles:
                    target //= 2
                    maxDoubles -= 1
                else:
                    break
            sol += 1
        return sol + target - 1
        