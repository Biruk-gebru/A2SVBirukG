# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for l,r in adjacentPairs:
            adj[l].append(r)
            adj[r].append(l)

        visited = set()
        answer = []
        start = [l for l,r in adj.items() if len(r) == 1][1]

        while start not in visited:
            answer.append(start)
            visited.add(start)
            for child in adj[start]:
                if child not in visited:
                    start = child
        
        return answer
                
