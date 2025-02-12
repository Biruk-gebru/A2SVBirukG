# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired_up= {}
        for i in range(len(names)):
            paired_up[heights[i]]=names[i]
        paired_up= (sorted(paired_up.items(),key=lambda item:item[0],reverse=True ))
        return [n[1] for n in paired_up]
        