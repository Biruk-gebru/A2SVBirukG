# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for l,r in adjacentPairs:
            adj[l].append(r)
            adj[r].append(l)
        
        start = [l for l,r in adj.items() if len(r)==1][0]
        sol = []
        def dfs(x, p):
            sol.append(x)
            for n in adj[x]:
                if n != p:
                    dfs(n,x)

        dfs(start, float('inf'))
        return sol