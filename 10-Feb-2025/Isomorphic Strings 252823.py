# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sC = defaultdict(str)
        sT = defaultdict(str)
        print(sC, sT)
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if sC[s[i]] == "" :
                    sC[s[i]] = t[i]
                if sT[t[i]] == "":
                    sT[t[i]] = s[i]
                if sC[s[i]] != t[i] or sT[t[i]] != s[i]:
                    return False
        return True
                

        
        