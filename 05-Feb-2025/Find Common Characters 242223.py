# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        sol = []
        for i in range(1,len(words)):
            c = Counter(words[i])
            count &= c
        for k,v in count.items():
            sol.extend(k*v)
        return sol

    
        
    