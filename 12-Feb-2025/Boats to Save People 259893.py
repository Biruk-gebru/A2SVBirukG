# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter = 0
        i,j=0, len(people)-1
        people.sort()
        while i<=j:
            if people[i] + people[j] <= limit:
                i+=1
            counter +=1
            j-=1
        return counter
        