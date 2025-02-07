# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        t = abs(target[0]) + abs(target[1])
        for g in ghosts:
            print(abs(g[0] - target[0]) + abs(g[1] - target[1]))
            if (abs(g[0] - target[0]) + abs(g[1] - target[1]) <= t):
                return False
        return True
    