# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        sol = ""
        while i < len(s):
            if i < len(s) - 2:
                if s[i+2] == "#":
                    ind = int(s[i]+s[i+1])
                    print(chr(int(s[i]+s[i+1])),int(s[i]+s[i+1]))
                    i += 2
                else:
                    ind = int(s[i])
                    print(chr(ind), ind)
            else:
                ind = int(s[i])
                print(chr(ind), ind)
            i += 1
            sol += chr(ind + 96)
        
        return sol

        