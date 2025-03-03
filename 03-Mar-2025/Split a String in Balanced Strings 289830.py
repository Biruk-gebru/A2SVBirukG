# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = Counter(s)
        sol = 0
        for i in range(len(s)):
            c[s[i]] -= 1
            if c["L"] == c["R"]:
                sol +=1
        return sol
        