# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(firstList), len(secondList)
        if n1==0 or n2==0:
            return []
        i=j=0
        sol=[]
        while i<n1 and j<n2:
            start=max(firstList[i][0],secondList[j][0])
            end=min(firstList[i][1],secondList[j][1])
            if start<=end:
                sol.append([start,end])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return sol


        