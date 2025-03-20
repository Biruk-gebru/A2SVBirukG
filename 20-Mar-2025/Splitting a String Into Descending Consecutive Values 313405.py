# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtracking(i, prev, k):
            if i == len(s):
                return k > 1
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                if prev == -1 or int(prev) - int(curr) == 1:
                    if backtracking(j + 1, curr, k+1):
                        return True
            return False
        return backtracking(0, -1 , 0)
