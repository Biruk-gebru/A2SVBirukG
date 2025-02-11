# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sm = sorted(points, key = lambda x : math.sqrt((x[1])**2 + (x[0])**2 ))
        sol = []
        for j in range(k):
            sol.append(sm[j])
        return sol
        