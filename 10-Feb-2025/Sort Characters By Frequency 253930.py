# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        c= Counter(s)
        l=sorted(c, key= c.get, reverse=True)
        print(l)
        sol = []
        for k in l:
            sol.extend(k * c[k])
        return "".join(sol)
        