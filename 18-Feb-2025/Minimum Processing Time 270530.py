# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        sol = float('-inf')
        count = 0
        psi = 0
        temp = 0
        for i in range(len(processorTime)):
            temp = 0
            count = 0
            while psi< len(tasks) and count < 4:
                count += 1
                temp = max(temp , processorTime[i] + tasks[psi])
                psi += 1
            sol = max(sol,temp)
        return sol
            
                

        