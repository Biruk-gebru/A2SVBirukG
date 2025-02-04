# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_c = Counter(s)
        sol = [x for x in s_c.values()]
        if len(set(sol)) == 1:
            return True
        return False
        