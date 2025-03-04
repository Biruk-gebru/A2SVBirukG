# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        
        arrow_pos = points[0][1] 
        arrow_count = 1 
        
        for i in range(1, len(points)):
            if arrow_pos >= points[i][0]:
                continue
            else:
                arrow_count += 1
                arrow_pos = points[i][1]
        
        return arrow_count
