# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for el in strs:
            temp = tuple(sorted(el))
            sol[temp].append(el)
        return [n for n in sol.values()]